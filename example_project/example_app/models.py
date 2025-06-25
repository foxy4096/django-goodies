from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Developer(models.Model):
    name = models.CharField(max_length=100)
    favorite_language = models.ForeignKey(
        Language, on_delete=models.SET_NULL, null=True, blank=True
    )
    known_languages = models.ManyToManyField(Language, related_name="developers", blank=True)

    def __str__(self):
        return self.name
