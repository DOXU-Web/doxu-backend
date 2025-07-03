from django.urls import path
from .views import CharacterListAPIView, CharacterDetailAPIView

urlpatterns = [
    path('characters/', CharacterListAPIView.as_view(), name='character-list'),
    path('characters/<int:id>/', CharacterDetailAPIView.as_view(), name='character-detail'),
]