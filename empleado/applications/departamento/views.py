from django.shortcuts import render
from django.views.generic import (ListView)
from django.views.generic.edit import FormView
from applications.personal.models import Empleado
from .models import Departamento
from .forms import NewDepartamentoForm

# Create your views here.
class DepartamentoListView(ListView):
    template_name = 'departamento/lista_departamentos.html'
    #model = Departamento  # Se elimina si se usa el metod get
    # Se puede usar una variable de contexto en vez de usar en pantalla el "object_list"
    #context_object_name = 'list_dep'
    ordering = 'name'

    def get_queryset(self):
        # Codigo que filtra lista de empleados desde la pantalla
        # El 'self.request.GET.get' nos permite recoger una variable desde el HTML
        # desde un <input> y un <button>
        clave = self.request.GET.get('kword', '')
        lista = Departamento.objects.filter(
            name__icontains=clave)
        return lista
    
class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'
    # Metodo que se ejecuta despues de validar y guardado los datos
    def form_valid(self, form): 
        # logica del proceso
        depa = Departamento(
            name = form.cleaned_data['departamento'],
            shor_name = form.cleaned_data['shortname']
        )
        depa.save()

        nombre = form.cleaned_data['nombres']
        apellido = form.cleaned_data['apellidos']
        
        Empleado.objects.create(
            first_name = nombre,
            last_name = apellido,
            job = '1',
            departamento = depa
        )
        # Este me genera un error
        #return super(NewDepartamentoForm,self).form_valid(form)
        return super().form_valid(form) 
