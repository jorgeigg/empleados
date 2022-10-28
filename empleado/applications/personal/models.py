from django.db import models
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField

# Create your models here.
"""Modelo de la tabla de la BD Habilidades"""
class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)
    # Defino algunas caracteristicas para el admin. de Django
    class Meta:
      verbose_name = 'Ability'  # Nombre de Columna singular
      verbose_name_plural = 'Abilities'  # Nombre en plural
      # Defino los titulos de las columnas de el admin. de Django

    def __str__(self):
      return str(self.id) + ' - ' + self.habilidad

"""Modelo de la tabla de la BD Empleado"""
class Empleado(models.Model):
    # Lista de seleccion de la columna job
    JOB_CHOICES = (
        ('0','Contractado'),
        ('1','Empleado'),
        ('2','Administrativo'),
        ('3','Ejecutivo'),
        ('4','Junta Directiva'),
        ('5','Jubilado'),
        ('6','Otros')
    )
    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    full_name = models.CharField('NombresCompleto', max_length=120, blank=True)
    job = models.CharField('TipoDeTrabajador', max_length=1, choices=JOB_CHOICES)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    image = models.ImageField('Foto', upload_to='empleado', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField(blank=True, null=True)
    
    # Defino algunas caracteristicas para el admin. de Django
    class Meta:
      verbose_name = 'Employee'  # Nombre de Columna singular
      verbose_name_plural = 'My Employees'  # Nombre en plural
      ordering = ['first_name', 'last_name']  # Ordenar como se ver los datos
      # Limito de manera general que no se repitan datos, no como con 'unique=' que es individual
      unique_together = ('first_name', 'last_name')

    # Defino los titulos de las columnas de el admin. de Django
    def __str__(self):
      return str(self.id) +' - '+ self.first_name +' - '+ self.last_name +' - '+ self.job +' - '+ str(self.departamento)