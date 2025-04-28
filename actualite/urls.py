from django.urls import path

from actualite import views 

urlpatterns = [
  
  path('', views.accueil_actualite, name="accueil_actualite"),
  path('actualite/ajouter/', views.ajouter_actualite, name='ajouter_actualite'),
  path('actualite/modifier/<slug:slug>/', views.modifier_actualite, name='modifier_actualite'),
  path('actualite/supprimer/<slug:slug>/', views.supprimer_actualite, name='supprimer_actualite'),

]