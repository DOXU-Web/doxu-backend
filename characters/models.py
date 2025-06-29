from django.db import models

class Character(models.Model):
    # Choix pour les classes de personnages
    CLASS_CHOICES = [
        ('guerrier', 'Guerrier'),
        ('mage', 'Mage'),
        ('assassin', 'Assassin'),
        ('archer', 'Archer'),
        ('paladin', 'Paladin'),
    ]
    
    # Champs essentiels seulement
    name = models.CharField(max_length=100, verbose_name="Nom")
    character_class = models.CharField(
        max_length=20, 
        choices=CLASS_CHOICES, 
        verbose_name="Classe"
    )
    description = models.TextField(max_length=500, verbose_name="Description")
    image = models.ImageField(
        upload_to='characters/', 
        verbose_name="Image",
        blank=True,  # Image optionnelle
        null=True
    )
    
    # Champs utiles pour l'organisation
    is_active = models.BooleanField(default=True, verbose_name="Actif")
    order = models.PositiveIntegerField(default=0, verbose_name="Ordre d'affichage")
    
    # Champs automatiques
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Créé le")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Modifié le")
    
    class Meta:
        verbose_name = "Personnage"
        verbose_name_plural = "Personnages"
        ordering = ['order', 'name']
    
    def __str__(self):
        return f"{self.name} ({self.character_class})"