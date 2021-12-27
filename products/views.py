from django.shortcuts import render
from .models import *

# Create your views here.
def product(request):
    produits = Produit.objects.all()
    return render(request, 'produit.html', {'produits' : produits})