from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .forms import (
    DeveloperForm,
    CustomUserChangeForm,
    CustomUserCreationForm,
    UserSearchForm,
    DevloperSearchForm
)
from .models import Developer


def index(request, id=None):
    """
    View to render the form.
    """
    form = DeveloperForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        print(form.cleaned_data)
        # Don't save the form, just return the cleaned data as JSON
        data = {
            "name": form.cleaned_data["name"],
            "favorite_language": form.cleaned_data["favorite_language"].name,
            "known_languages": [
                lang.name for lang in form.cleaned_data["known_languages"]
            ],
        }
        return JsonResponse(data)

    if id:
        # If an ID is provided, fetch the existing Developer instance
        developer = get_object_or_404(Developer, id=id)
        form = DeveloperForm(instance=developer)

    urform = CustomUserCreationForm()
    ucform = CustomUserChangeForm(instance=request.user)
    usform = UserSearchForm(request.GET or None)
    dsform = DevloperSearchForm(request.GET or None)

    return render(
        request,
        "index.html",
        {
            "form": form,
            "urform": urform,
            "ucform": ucform,
            "usform": usform,
            "dsform": dsform,
        },
    )
