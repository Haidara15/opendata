from django import forms

from django import forms

class ContactForm(forms.Form):
    nom = forms.CharField(
        label="Nom",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    prenom = forms.CharField(
        label="Prénom",
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    email = forms.EmailField(
        label="Votre Email",
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
    )
    objet = forms.CharField(
        label="Objet",
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    description = forms.CharField(
        label="Votre Besoin",
        widget=forms.Textarea(attrs={ 'class': 'form-control', 'rows': 4}),
    )
