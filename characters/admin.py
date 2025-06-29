from django.contrib import admin
from .models import Character

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    # Champs affichés dans la liste
    list_display = ['name', 'character_class', 'is_active', 'order', 'created_at']
    
    # Filtres sur le côté
    list_filter = ['character_class', 'is_active']
    
    # Barre de recherche
    search_fields = ['name', 'description']
    
    # Champs modifiables directement dans la liste
    list_editable = ['is_active', 'order']
    
    # Organisation simple du formulaire
    fieldsets = (
        ('Informations du personnage', {
            'fields': ('name', 'character_class', 'description', 'image')
        }),
        ('Paramètres', {
            'fields': ('is_active', 'order'),
            'classes': ('collapse',)
        })
    )
    
    ordering = ['order', 'name']