from django.contrib import admin

# Register your models here.
from .models import Empleado, Habilidades

admin.site.register(Habilidades)

# Defino los titulos de las columnas de el admin. de Django
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'departamento',
        'job',
        'full_name',
        )
    search_fields =(
        'first_name',
        'last_name',
    )
    # Permite crear funciones adicionales en la vista de los registros en la tabla Empleado
    def full_name(selt, obj):
        # Toda la operacion
        #print(obj)
        return obj.first_name+' '+obj.last_name
    # Permite filtrar los registros o filas en la tabla Empleado
    list_filter = ('departamento', 'job', 'habilidades')
    # Filtro Horizontal para Habilidades dentro de la tabla Empleado
    filter_horizontal = ('habilidades',)

admin.site.register(Empleado,EmpleadoAdmin)

