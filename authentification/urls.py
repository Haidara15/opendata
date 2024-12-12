from django.contrib import admin

from django.urls import path

from .views import page_connexion, page_inscription,deconnection

urlpatterns = [

    path('connexion/', page_connexion, name="connexion"),

    path('inscription/',page_inscription, name="inscription"),

    path('deconnexion/',deconnection, name="deconnexion"),

] 