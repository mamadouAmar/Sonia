from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.
def product(request):
    template = loader.get_template('produit.html')
    return HttpResponse(template.render(request = request))