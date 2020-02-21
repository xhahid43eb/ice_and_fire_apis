from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=250, null=False, unique=True)

    def __str__(self):
        return self.name
