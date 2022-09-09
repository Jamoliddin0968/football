from django.db import models
from club.models import Club

"""
positions = models.TextChoices('positions',"gk cb rb lb dmf cmf lmf amf rmf rwf lwf ss cf")
"""

class Player(models.Model):
    name = models.CharField(max_length=60)
    birth_date = models.DateField()

    birth_place = models.CharField(max_length=60)
    weight = models.FloatField()
    heigth = models.IntegerField(verbose_name="heigth(cm)")
    current_club = models.ForeignKey(Club,on_delete=models.CASCADE)
    image = models.ImageField()

    class Meta:
        verbose_name = "Futbolchi"
        verbose_name_plural = "Futbolchilar"



