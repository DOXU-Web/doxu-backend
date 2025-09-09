from rest_framework import serializers
from .models import Character

class CharacterSerializer(serializers.ModelSerializer):
   
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Character
        fields = [
            "id",
            "name",
            "character_class",
            "detailed_description",
            "image_url",
            "is_active",
            "order",
        ]

    def get_image_url(self, obj):
        if getattr(obj, "image", None):
            request = self.context.get("request")
            return request.build_absolute_uri(obj.image.url) if request else obj.image.url
        return None
