from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=250, null=False, unique=True)
    country_code = models.CharField(max_length=2, unique=True, default='PK')

    def __str__(self):
        return self.name
