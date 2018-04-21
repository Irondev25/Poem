from django import forms
from .models import Poem
from django.utils.text import slugify

class PoemForm(forms.ModelForm):
    class Meta:
        model=Poem
        #experiment with exclude=['slug'] 
        exclude = ['slug'] 

    def save(self):
        instance = super().save(commit=False)
        instance.slug = slugify(instance.title)+ '-' + slugify(instance.poet)
        instance.save()
        return instance



