from django.forms import widgets
from django.urls import reverse_lazy
from django.apps import apps
import json


class BaseModelAutoCompleteWidget(widgets.TextInput):
    """
    Base widget for model autocomplete fields.
    This is not meant to be used directly, but as a base for specific implementations.
    """

    template_name = "autocomplete/autocomplete_widget.html"

    class Media:
        js = [
            "django_goodies/htmx/htmx.min.js",
            "django_goodies/autocomplete/hyperscript.min.js",  # optional
        ]
        css = {
            "all": [
                "django_goodies/autocomplete/autocomplete.css",
            ]
        }

    def __init__(
        self,
        *,
        app_label,
        model_name,
        model_field_name,
        fallback_queryset=None,
        result_element=None,
        attrs=None,
    ):
        """
        Initializes the autocomplete widget with model information.

        Args:
            app_label (str): Django app label where the model lives.
            model_name (str): Model class name (case-insensitive).
            model_field_name (str): Field to display in the search result (e.g., 'name').
            fallback_queryset (QuerySet): Optional static fallback list for non-JS clients.
            attrs (dict): HTML attributes to override.
        """
        self.app_label = app_label
        self.model_name = model_name
        self.model_field_name = model_field_name
        self.result_element = result_element
        self.lookup_url = reverse_lazy(
            "autocomplete:generic",
            kwargs={
                "app_label": app_label,
                "model_name": model_name,
                "model_field_name": model_field_name,
            },
        )
        self.fallback_queryset = fallback_queryset or []

        base_attrs = {
            "autocomplete": "off",
            "hx-get": self.lookup_url,
            "hx-trigger": "keyup changed delay:300ms",
            "hx-swap": "innerHTML",
            "hx-cache": "false",
        }

        if attrs:
            base_attrs.update(attrs)

        super().__init__(base_attrs)

    def get_model_instance(self, value):
        """Helper method to get the model instance for a given value."""
        if not value:
            return None
        try:
            model = apps.get_model(self.app_label, self.model_name)
            return model.objects.get(pk=value)
        except (model.DoesNotExist, ValueError):
            return None

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        results_id = f"results_{self.result_element or name}"
        context["widget"]["attrs"]["id"] = f"id_{name}_autocomplete"
        context["widget"]["attrs"]["hx-target"] = f"#{results_id}"
        context["widget"]["results_id"] = results_id
        context["widget"]["attrs"]["hx-vals"] = json.dumps(
            {
                "form_field_name": name,
                "is_multiple": self.is_multiple,
            }
        )

        # Normalize value(s)
        if self.is_multiple:
            selected = [self.get_model_instance(v) for v in value or []]
        else:
            selected = [self.get_model_instance(value)] if value else []

        if self.is_multiple and value:
            context["widget"]["selected_objects"] = self._get_selected_objects(value)
        elif value:
            context["widget"]["selected_object"] = self._get_selected_object(value)

        context["widget"].update(
            {
                "app_label": self.app_label,
                "model_name": self.model_name,
                "field_name": self.model_field_name,
                "lookup_url": self.lookup_url,
                "fallback_queryset": self.fallback_queryset,
                "selected": value,
                "is_multiple": self.is_multiple,
                "form_field_name": name,
            }
        )
        return context

    def _get_selected_objects(self, value):
        # handles a list of IDs or queryset
        model = apps.get_model(self.app_label, self.model_name)
        if hasattr(value, "__iter__"):
            return model.objects.filter(pk__in=value)
        return []

    def _get_selected_object(self, value):
        model = apps.get_model(self.app_label, self.model_name)
        try:
            return model.objects.get(pk=value)
        except model.DoesNotExist:
            return None


class SingleModelAutoCompleteWidget(BaseModelAutoCompleteWidget, widgets.Select):
    is_multiple = False


class MultipleModelAutoCompleteWidget(
    BaseModelAutoCompleteWidget, widgets.SelectMultiple
):
    is_multiple = True
