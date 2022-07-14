from django import forms
from .models import Art


class ArtForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['art_id'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['art'].widget.attrs.update({'class': 'form-control'})
        self.fields['title'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['artist'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['quantity'].widget.attrs.update({'class': 'textinput form-control', 'min': '0'})
        self.fields['price'].widget.attrs.update({'class': 'textinput form-control', 'min': '0'})

    class Meta:
        model = Art
        fields = ['art_id', 'art', 'title', 'artist', 'quantity', 'price']