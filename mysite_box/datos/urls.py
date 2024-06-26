from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('form/', views.formulariobasico, name='form'),
    path('historico/', views.historico, name='historico'),
    path('edad/', views.otravista, name='edad'),
    path('profesionales/', views.formularioprofesionales, name='profesionales'),
    path('todos/', views.todoslosprofesionalesvista, name='todos'),
    path('uno/', views.justone, name='uno'),
    path('dos/', views.crear_profesional, name='dos'),
]