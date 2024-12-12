from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
    
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
    first_name = forms.CharField(label="",
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Prénom'
        })
    )
    last_name = forms.CharField(label="",
        widget=forms.TextInput(attrs={
            'class': 'form-control', 
            'placeholder': 'Nom'
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
