from django import forms
from .models import Thematiques, SousThematique

class CommentForm(forms.Form):
    content = forms.CharField(
        label='',
        widget=forms.Textarea(attrs={'class': 'form-control w-100', 'rows': 3, 'placeholder': 'Écrire un commentaire...'})
    )
    parent_id = forms.IntegerField(widget=forms.HiddenInput, required=False)



class ThematiquesForm(forms.ModelForm):
    class Meta:
        model = Thematiques
        fields = ['titre', 'description', 'image']
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }




class SousThematiqueForm(forms.ModelForm):
    class Meta:
        model = SousThematique
        fields = ['thematique_parente', 'titre', 'description_sous_thematique', 'periodicite', 'csv_file']
        widgets = {
            'thematique_parente': forms.Select(attrs={'class': 'form-control'}),
            'titre': forms.TextInput(attrs={'class': 'form-control'}),
            'description_sous_thematique': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'periodicite': forms.TextInput(attrs={'class': 'form-control'})
        }




########## Actualité ######### 

from django import forms
from .models import Actualite

from django import forms
from .models import Actualite

class ActualiteForm(forms.ModelForm):
    class Meta:
        model = Actualite
        fields = ['titre', 'description', 'image']

        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

