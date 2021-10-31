from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def afficher_home(request):

    template = loader.get_template('index.html')
    return HttpResponse(template.render(request = request))
