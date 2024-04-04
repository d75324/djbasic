from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('form/', views.formulariobasico, name='form'),
    path('historico/', views.historico, name='historico'),
]