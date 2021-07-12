from django.db import models

# Create your models here.
class Produit(models.Model):
    libelle = models.CharField((""), max_length=100)
    prix = models.FloatField((""))
    description = models.TextField((""))

    class Meta:
        verbose_name = "Produit"
        verbose_name_plural = "Produits"

    def __str__(self):
        return self.name


class Assets(models.Model):
    nom = models.CharField((""), max_length=50)
    date_ajout = models.DateField((""), auto_now=False, auto_now_add=False)
    produit = models.ForeignKey("products.Produit", verbose_name=(""), on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Asset"
        verbose_name_plural = "Assets"

    def __str__(self):
        return nom

    


