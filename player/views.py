from django.shortcuts import render

from rest_framework.generics import CreateAPIView
from .serializers import PlayerSerializer
from .models import Player

class PlayerList(CreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


