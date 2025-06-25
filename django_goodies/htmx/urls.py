from django.urls import path
from . import views

app_name = "goodies_htmx"
urlpatterns = [
    path("js-check/", views.js_check, name="js_check"),
]
