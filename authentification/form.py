from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']  # Suppression de first_name et last_name
    
    # Définir des attributs pour chaque champ du formulaire avec placeholders

    username = forms.CharField(label="",
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': "Nom d'utilisateur"
        })
    )
    email = forms.EmailField(label="",
        widget=forms.EmailInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Adresse e-mail'
        })
    )
    
    password1 = forms.CharField(label="",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Mot de passe'
        })
    )
    password2 = forms.CharField(label="",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Confirmer votre mot de passe'
        })
    )
