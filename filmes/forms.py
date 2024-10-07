from django import forms
from .models import ListFilmes, Filme

class ListFilmesForm(forms.ModelForm):
    class Meta:
        model = ListFilmes
        fields = '__all__'

class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = '__all__'