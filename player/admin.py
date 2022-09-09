from django.contrib import admin
from .models import Player

class PlayerConfig(admin.ModelAdmin):
    list_display = ["name","current_club"]


admin.site.register(Player,PlayerConfig)
