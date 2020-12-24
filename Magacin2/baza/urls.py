from django.urls import path,re_path
from . import views

urlpatterns = [
    path('', views.index, name='baza_index'),
    path('fp/',views.fProizvodjac,name='baza_fProizvodjac'),
]

