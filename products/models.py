from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.
class Produit(models.Model):
    libelle = models.CharField(("libelle"), max_length=100)
    prix = models.FloatField(("prix"))
    mode_d_emploi = models.TextField(("mode d'emploi"), default = "", blank = True, null=True)
    ingredients = models.TextField(("ingredients"), default = "", blank = True, null=True)
    image = models.ImageField(("image"), upload_to="produits/images/", height_field=None, width_field=None, max_length=None, null=True, blank=True)
    imageUrl = models.CharField((""), max_length=200, null=True, blank=True)

    class Meta:
        verbose_name = "Produit"
        verbose_name_plural = "Produits"

    def __str__(self):
        return self.libelle


class Assets(models.Model):
    asset = models.ImageField(("image"), upload_to="assets/images/", height_field=None, width_field=None, max_length=None, default="")    
    date_ajout = models.DateTimeField(("date"), auto_now=False, auto_now_add=False, default = timezone.now)
    produit = models.ForeignKey("Produit", verbose_name=("produit"), on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Asset"
        verbose_name_plural = "Assets"

    def __str__(self):
        return str(self.date_ajout)