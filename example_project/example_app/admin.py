from django.contrib import admin
from .models import Developer, Language
from .forms import DeveloperForm


@admin.register(Developer)
class DevloperAdmin(admin.ModelAdmin):
    form = DeveloperForm
    list_display = [
        "name",
        "favorite_language",
    ]


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    search_fields = [
        "name",
    ]
