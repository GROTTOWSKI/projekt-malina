
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/Marka/<int:pk>/',views.detail_Marka, name='detail_Marka'),
    path('detail/Typ/<int:pk>/', views.detail_Typ, name='detail_Typ'),
    path('detail/Osprzęt/<int:pk>/', views.detail_Osprzęt, name='detail_Osprzęt'),
    path('detail/Model/<int:pk>/',views.detail_Model, name='detail_Model'),
    path('bootstrap/',views.bootstrap, name='bootstrap'),
    path('Marki/', views.Marki_lista, name='Marki-lista'),
    path('Typy/', views.Typy_lista, name='Typy-lista'),
    path('Osprzęty/', views.Osprzęty_lista, name='Osprzęty-lista'),
    path('Modele/', views.Modele_lista, name='Modele-lista'),
    path('zapisano/', views.zapisano, name='zapisano'),
    path('dodaj-Marka/',views.dodaj_Marka, name='dodaj-Marka'),
    path('dodaj-Typ/',views.dodaj_Typ, name='dodaj-Typ'),
    path('dodaj-Osprzet/',views.dodaj_Osprzęt, name='dodaj-Osprzęt'),
    path('dodaj-Model/',views.dodaj_Model, name='dodaj-Model'),
]