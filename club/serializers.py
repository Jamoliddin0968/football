from .models import Club

from rest_framework import serializers

class ClubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = "__all__"

class ClubShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Club
        fields = ("id","name")