from django.db import models

# Create your models here.
class DepenseModel(models.Model):
    produit = models.CharField((""), max_length=50)
    somme_depense = models.FloatField((""))
    date_depense = models.DateTimeField((""), auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = "Depense"
        verbose_name_plural = "Depenses"

    def __str__(self):
        return produit


    def depense_journalier(jour):
        pass
    
    def depense_hebdomadaire(jour):
        pass

    def depense_mensuelle(mois):
        pass
