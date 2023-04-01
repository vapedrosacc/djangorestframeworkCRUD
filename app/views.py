from rest_framework import viewsets
from app import serializers
from app.models import GameList

class GameListViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.GameListSerializer
    queryset = GameList.objects.all()