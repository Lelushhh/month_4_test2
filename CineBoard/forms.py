from django import forms
from .models import Movies

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = ['name_movie', 'image', 'description', 'jenre_movies']