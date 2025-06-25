# urls.py

from django.urls import path
from . import views

app_name = "autocomplete"
urlpatterns = [
    path(
        "search/<str:app_label>/<str:model_name>/<str:model_field_name>/",
        views.generic_model_autocomplete,
        name="generic",
    ),
]
