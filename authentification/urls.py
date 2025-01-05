from django.contrib import admin

from django.urls import path

from .views import page_connexion, page_inscription,deconnection, verify_email

from django.contrib.auth import views as auth_views

urlpatterns = [

    path('connexion/', page_connexion, name="connexion"),

    path('inscription/',page_inscription, name="inscription"),

    path('deconnexion/',deconnection, name="deconnexion"),

    path('verification_email/<uidb64>/<token>/', verify_email, name='verification_email'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='authentification/password_reset_form.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='authentification/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='authentification/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='authentification/password_reset_complete.html'), name='password_reset_complete'),



] 