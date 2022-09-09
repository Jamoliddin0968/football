from django.db import models


class Club(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=3)
    logo = models.ImageField()
    created_name = models.DateField()

    def __str__(self):
        return self.short_name
