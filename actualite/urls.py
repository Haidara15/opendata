from django.urls import path

from actualite import views 

urlpatterns = [
  
  path('', views.accueil_actualite, name="accueil_actualite"),
  path('ajouter/', views.ajouter_actualite, name='ajouter_actualite'),
  path('modifier/<slug:slug>/', views.modifier_actualite, name='modifier_actualite'),
  path('supprimer/<slug:slug>/', views.supprimer_actualite, name='supprimer_actualite'),

]