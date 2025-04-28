from django.urls import path

from contact import views 

urlpatterns = [
  
  path('', views.accueil_contact, name="accueil_contact"),

]