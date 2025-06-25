from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("example_app.urls")),
    path('autocomplete/', include("django_goodies.autocomplete.urls")),
    path("admin/", admin.site.urls),
]
