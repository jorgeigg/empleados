from django.db import models

# Create your models here.
class Departamento(models.Model):
    name = models.CharField('Nombre',max_length=50)
    shor_name = models.CharField('NombreCorto',max_length=20, unique=True)
    anulate = models.BooleanField('Anulado', default=False)

    # Defino algunas caracteristicas para el admin. de Django
    class Meta:
      verbose_name = 'Department' # Nombre de Columna singular
      verbose_name_plural = 'My Departments' # Nombre en plural
      ordering = ['id'] # Ordenar como se ver los datos
      # Limito de manera general que no se repitan datos, no como con 'unique=' que es individual
      unique_together = ('name','shor_name')

    # Defino los titulos de las columnas de el admin. de Django
    def __str__(self):
      #return str(self.id) +' - '+ self.name +' - '+ self.shor_name +' - '+ str(self.anulate)
      return self.name