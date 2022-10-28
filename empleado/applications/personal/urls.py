"""
"""
from django.urls import path
from . import views

app_name = 'personal_app'
urlpatterns = [
    path('', views.InicioView.as_view(), name='inicio'),
    path('listar_todos_empleados/', views.ListAllEmpleados.as_view(), name='empleados_all'),
    path('listar_by_areas/<shorname>/', views.ListByAreaEmpleados.as_view(), name='empleados_area'),
    path('listar_empleados/', views.ListEmpleadosAdmin.as_view(), name='empleados_admin'),
    path('listar_by_kword/', views.ListEmpleadosByKword.as_view()),
    path('listar_by_habilidades/', views.ListHabilidadesEmpleados.as_view()),
    path('ver_empleado/<pk>/', views.EmpleadosDetailView.as_view(), name='empleado_detail'),
    path('add_empleado/', views.EmpleadoCreateView.as_view(), name='empleado_add'),
    path('success/', views.SuccessView.as_view(), name='correcto'),
    path('update_empleado/<pk>/', views.EmpleadoUpdateView.as_view(), name='modificar'),
    path('delete_empleado/<pk>/', views.EmpleadoDeleteView.as_view(), name='eliminar'),
]
