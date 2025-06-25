from django.apps import apps
from django.http import HttpResponseBadRequest

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.paginator import Paginator
from django_goodies.htmx.decorators import htmx_only


@htmx_only
@login_required
def generic_model_autocomplete(request, app_label, model_name, model_field_name):
    """
    Generic model autocomplete view that retrieves model instances based on a query.
    """
    form_field_name = request.GET.get("form_field_name")
    query = request.GET.get(f"{form_field_name}_autocomplete", "").strip()
    is_multiple = request.GET.get("is_multiple", "false").lower() == "true"
    page = request.GET.get("page", 1)

    if not all([app_label, model_name, model_field_name]):
        return HttpResponseBadRequest("Missing required parameters.")

    model_path = f"{app_label}.{model_name}"
    allowed_fields = settings.DJANGO_GOODIES.get("ALLOWED_AUTOCOMPLETE_MODELS", {}).get(
        model_path
    )

    if not allowed_fields or model_field_name not in allowed_fields:
        return HttpResponseBadRequest("Invalid model or field name.")

    try:
        model = apps.get_model(app_label, model_name)
        filter_kwargs = {f"{model_field_name}__icontains": query}
        results = model.objects.filter(**filter_kwargs).order_by(model_field_name)
        paginator = Paginator(results, 10)
        results = paginator.get_page(page)

    except Exception as e:
        return HttpResponseBadRequest(f"Error retrieving model: {str(e)}")

    return render(
        request,
        "autocomplete/autocomplete_results.html",
        {
            "results": results,
            "form_field_name": form_field_name,
            "is_multiple": is_multiple,
            "query": query,
            "results_id": f"results_{form_field_name}",
        },
    )
