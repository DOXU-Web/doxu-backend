from django.db import models

class Character(models.Model):
    CLASS_CHOICES = [
        ('Rushdown', 'Rushdown'),
        ('Duo Character', 'Duo Character'),
        ('Set up', 'Set up'),
    ]
    
    name = models.CharField(max_length=100, verbose_name="Nom")
    character_class = models.CharField(
        max_length=20, 
        choices=CLASS_CHOICES, 
        verbose_name="Classe"
    )
   
    detailed_description = models.TextField(
        verbose_name="Description détaillée",
        help_text="Description complète affichée sur la page du personnage",
        blank=True
    )
    image = models.ImageField(
        upload_to='characters/', 
        verbose_name="Image",
        blank=True,
        null=True
    )
    
    is_active = models.BooleanField(default=True, verbose_name="Actif")
    order = models.PositiveIntegerField(default=0, verbose_name="Ordre d'affichage")
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Créé le")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Modifié le")
    
    class Meta:
        verbose_name = "Personnage"
        verbose_name_plural = "Personnages"
        ordering = ['order', 'name']
    
    def __str__(self):
        return f"{self.name} ({self.character_class})"