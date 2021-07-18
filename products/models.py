from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.
class Produit(models.Model):
    libelle = models.CharField(("libelle"), max_length=100)
    prix = models.FloatField(("prix"))
    mode_d_emploi = models.TextField(("mode_d_emploi"))
    ingredients = models.TextField(("ingredients"))

    class Meta:
        verbose_name = "Produit"
        verbose_name_plural = "Produits"

    def __str__(self):
        return self.libelle


class Assets(models.Model):
    asset = models.ImageField(("image"), upload_to=None, height_field=None, width_field=None, max_length=None)    
    date_ajout = models.DateTimeField(("date"), auto_now=False, auto_now_add=False, default = timezone.now)
    produit = models.ForeignKey("Produit", verbose_name=("produit"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Asset"
        verbose_name_plural = "Assets"

    def __str__(self):
        return nom

    


