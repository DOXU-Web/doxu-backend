from rest_framework import generics
from .models import Character
from .serializers import CharacterSerializer

class CharacterListAPIView(generics.ListAPIView):
    serializer_class = CharacterSerializer

    def get_queryset(self):
        return Character.objects.filter(is_active=True).order_by("order", "name")

class CharacterDetailAPIView(generics.RetrieveAPIView):
    queryset = Character.objects.filter(is_active=True)
    serializer_class = CharacterSerializer
    lookup_field = "id"
