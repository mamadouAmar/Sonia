from django.http.response import HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.
def menu(request):
    page_menu = loader.get_template('menu.html')
    return HttpResponse(page_menu.render(request = request))