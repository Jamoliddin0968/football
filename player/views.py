from django.shortcuts import render

from rest_framework.generics import ListAPIView
from .serializers import PlayerSerializer
from .models import Player
from .permissions import myPermission
class PlayerList(ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = (myPermission,)


