from rest_framework import generics
from rest_framework.response import Response
from .models import Character
from .serializers import CharacterSerializer, CharacterListSerializer

class CharacterListAPIView(generics.ListAPIView):
    """
    API pour récupérer la liste des personnages actifs
    """
    serializer_class = CharacterListSerializer
    
    def get_queryset(self):
        # Retourner seulement les personnages actifs, triés par ordre
        return Character.objects.filter(is_active=True).order_by('order', 'name')

class CharacterDetailAPIView(generics.RetrieveAPIView):
    """
    API pour récupérer les détails d'un personnage
    """
    queryset = Character.objects.filter(is_active=True)
    serializer_class = CharacterSerializer
    lookup_field = 'id'