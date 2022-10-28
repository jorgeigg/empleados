from django.shortcuts import render
from django.views.generic import (TemplateView, 
ListView, CreateView)
# Importar models
from .models import Prueba
from .forms import PruebaForm


# Create your views here.
# Crear una vista con un metodo Generico
class PruebaView(TemplateView):
    template_name = 'home/prueba.html'
# Crear una vista con un metodo Generico usando Foundation Framework
class ResumenFoundationView(TemplateView):
    template_name = 'home/resume_foundation.html'
# Crear una vista y listar con un metodo Generico
class PruebaListView(ListView):
   template_name = 'home/lista.html'
   context_object_name = 'listanumeros'
   queryset = ['0','10','20','30']
# Crear una vista y listar con un metodo Generico
class ListaPrueba(ListView):
   template_name = 'home/lista_prueba.html'
   model = Prueba
   context_object_name = 'lista'
# Crear una vista y listar con un metodo Generico
class PruebaCreateView(CreateView):
   template_name = 'home/add.html'
   model = Prueba
   form_class = PruebaForm
   success_url = '/'