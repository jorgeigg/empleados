from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ( 
    ListView, 
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
    )
# Create your views here.

# Models de la BD Empleado
from .models import Empleado
# Forms de Empleado
from .forms import EmpleadoForm

# Vista que carga la pagina de inicio
class InicioView(TemplateView):
    template_name = 'inicio.html'


# Lista todos los empleados de la empresa
class ListAllEmpleados(ListView):
    template_name = 'personal/list_all.html'
    paginate_by = 10
    ordering = 'first_name'
    #model = Empleado # Se elimina si se usa el metod get
    # Se puede usar una variable de contexto en vez de usar en pantalla el "object_list"
    #context_object_name = 'list_all'

    def get_queryset(self):
    # Codigo que filtra lista de empleados desde la pantalla
    # El 'self.request.GET.get' nos permite recoger una variable desde el HTML
    # desde un <input> y un <button>
        clave = self.request.GET.get('kword', '')
        lista = Empleado.objects.filter(
            full_name__icontains=clave)
        return lista


# Lista todos los empleados por area de la empresa
# usando una variabla en el URL
class ListByAreaEmpleados(ListView):
    template_name = 'personal/list_by_areas.html'
    paginate_by = 10
    ordering = 'first_name'

    def get_queryset(self):
        # Codigo que filtra lista de empleados desde la pantalla
        # El 'self.kwargs' nos permite recoger una variable desde el URL del HTML
        area = self.kwargs['shorname'] 
        lista = Empleado.objects.filter(
            departamento__shor_name= area)
        return lista


# Lista todos los empleados de la empresa
class ListEmpleadosAdmin(ListView):
    template_name = 'personal/list_empleados.html'
    paginate_by = 5
    ordering = 'first_name'
    model = Empleado # Se elimina si se usa el metod get
    # Se puede usar una variable de contexto en vez de usar en pantalla el "object_list"
    context_object_name = 'list_admin'


# Lista todos los empleados por nombre
# usando una variabla en un campo dentro del HTML
class ListEmpleadosByKword(ListView):
    template_name = 'personal/list_by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        # Codigo que filtra lista de empleados desde la pantalla
        # El 'self.request.GET.get' nos permite recoger una variable desde el HTML
        # desde un <input> y un <button>
        clave = self.request.GET.get('kword','')
        lista = Empleado.objects.filter(
                first_name=clave)
        return lista


# Lista todos los empleados por habilidades
# usando una variabla en un campo dentro del HTML
class ListHabilidadesEmpleados(ListView):
    template_name = 'personal/list_by_habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        # Codigo que filtra lista de empleados desde la pantalla
        # El 'self.request.GET.get' nos permite recoger una variable desde el HTML
        # desde un <input> y un <button>
        # El 'objects.get' nos permite buscar un emplado y luego mostrar todas sus habilidades
        clave = self.request.GET.get('kword', '')
        empleado = Empleado.objects.get(id=clave)
        return empleado.habilidades.all()


class EmpleadosDetailView(DetailView):
    template_name = 'personal/detail_empleado.html'
    model = Empleado
    # Metodo para enviar alguna otra informacion a la pantalla
    def get_context_data(self, **kwargs):
        context = super(EmpleadosDetailView,self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes' 
        return context

 
class SuccessView(TemplateView):
    template_name = 'personal/success.html'


class EmpleadoCreateView(CreateView):    
    template_name = 'personal/add.html'
    model = Empleado
    form_class =EmpleadoForm
    #fields = ['first_name', 'last_name', 'job','departamento', 'habilidades', 'image', 'hoja_vida']
    #fields = ("__all__") # Le indicas todas las columnas de la tabla
    # Cuando se usa "from_class" no es necesario utilizar el "fields" y detallar los campos
    #success_url = '.' # Le indicas la misma pagina o pantalla HTML
    # Se direcciona a otra pantalla
    #success_url = 'http://127.0.0.1:8000/listar_todos_empleados/' 
    #success_url = '/success' # No es la mejor manera de indicarlo
    success_url = reverse_lazy('personal_app:empleados_admin') # Mejor metodo de indicarlo

    # Metodo que se ejecuta despues de validar y guardado los datos
    def form_valid(self, form): 
        # logica del proceso
        # Creamos una variable que guarde los datos del formulario (una copia), los datos ya estan
        # guardados en la BD
        empleado = form.save(commit=False)  # El 'commit=False' no permite que se guarde
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        # Despues de modificar se salva en la BD
        empleado.save()
        return super(EmpleadoCreateView,self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    template_name = 'personal/update.html'
    model = Empleado
    fields = ['first_name', 'last_name', 'job',
              'departamento', 'habilidades']
    success_url = reverse_lazy('personal_app:empleados_admin')

    # Metodo que se ejecuta antes de validar y guardar los datos
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('*********POST*********')
        print(request.POST) # Se crea como un diccionario
        print('******************')
        print(request.POST['last_name']) # Se consulta como un diccionario
        return super().post(request, *args, **kwargs)


class EmpleadoDeleteView(DeleteView):  
    template_name = 'personal/delete.html'
    model = Empleado
    success_url = reverse_lazy('personal_app:empleados_admin')


