from django import forms
from .models import Developer, Language
from django_goodies.autocomplete.widgets import (
    SingleModelAutoCompleteWidget,
    MultipleModelAutoCompleteWidget,
)


class DeveloperForm(forms.ModelForm):
    known_languages = forms.ModelMultipleChoiceField(
        queryset=Language.objects.all(),
        required=False,
        label="Known Languages",
        widget=MultipleModelAutoCompleteWidget(
            app_label="example_app",
            model_name="Language",
            model_field_name="name",
            fallback_queryset=Language.objects.all(),
        ),
    )

    favorite_language = forms.ModelChoiceField(
        queryset=Language.objects.all(),
        required=False,
        label="Favorite Language",
        widget=SingleModelAutoCompleteWidget(
            app_label="example_app",
            model_name="Language",
            model_field_name="name",
            fallback_queryset=Language.objects.all(),
        ),
    )

    class Meta:
        model = Developer
        fields = "__all__"
        widgets = {
            "name": forms.TextInput(attrs={"class": "input"}),
        }


from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["username", "email", "password1", "password2"]


class CustomUserChangeForm(UserChangeForm):

    groups = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        required=False,
        label="Groups",
        widget=MultipleModelAutoCompleteWidget(
            app_label="auth",
            model_name="Group",
            model_field_name="name",
            fallback_queryset=User.objects.all(),
        ),
    )

    permissions = forms.ModelMultipleChoiceField(
        queryset=User.objects.all(),
        required=False,
        label="Permissions",
        widget=MultipleModelAutoCompleteWidget(
            app_label="auth",
            model_name="Permission",
            model_field_name="name",
            fallback_queryset=User.objects.all(),
        ),
    )

    class Meta(UserChangeForm.Meta):
        model = User
        fields = "__all__"
        widgets = {
            "username": forms.TextInput(attrs={"class": "input"}),
            "email": forms.EmailInput(attrs={"class": "input"}),
        }

class UserSearchForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        required=False,
        label="Username",
        widget=SingleModelAutoCompleteWidget(
            app_label="auth",
            model_name="User",
            model_field_name="username",
            fallback_queryset=User.objects.all()
        ),
    )


class DevloperSearchForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=False,
        label="Developer Name",
        widget=SingleModelAutoCompleteWidget(
            app_label="example_app",
            model_name="Developer",
            model_field_name="name",
            fallback_queryset=Developer.objects.all()
        ),
    )
    
    favorite_language = forms.ModelChoiceField(
        queryset=Language.objects.all(),
        required=False,
        label="Favorite Language",
        widget=SingleModelAutoCompleteWidget(
            app_label="example_app",
            model_name="Language",
            model_field_name="name",
            fallback_queryset=Language.objects.all(),
            result_element="favorite_language_search",
        ),
    )