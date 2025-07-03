from rest_framework import serializers
from .models import Character

class CharacterSerializer(serializers.ModelSerializer):
    # Champ calculé pour l'URL de l'image
    image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Character
        fields = [
            'id',
            'name', 
            'character_class', 
            'description',
            'detailed_description',
            'image',
            'image_url',
            'is_active',
            'order'
        ]
    
    def get_image_url(self, obj):
        """Retourne l'URL complète de l'image"""
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None

class CharacterListSerializer(serializers.ModelSerializer):
    """Version pour la liste des personnages - MAINTENANT AVEC description détaillée"""
    image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Character
        fields = [
            'id', 
            'name', 
            'character_class', 
            'description', 
            'detailed_description',
            'image_url', 
            'order'
        ]
    
    def get_image_url(self, obj):
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None