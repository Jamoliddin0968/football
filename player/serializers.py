from rest_framework import serializers
from club.serializers import ClubSerializer ,ClubShortSerializer
from .models import Player
from club.models import Club

class PlayerSerializer(serializers.ModelSerializer):
    current_club = serializers.PrimaryKeyRelatedField(queryset = Club.objects.all())
    class Meta:
        model = Player
        fields = "__all__"
