from django.urls import path
from .views import PlayerList

urlpatterns = [
    path("",PlayerList.as_view()),
]