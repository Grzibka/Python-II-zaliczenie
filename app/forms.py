from django import forms
from .models import Entry, Photo

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['title', 'content']

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image']
