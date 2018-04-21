from django import forms
from .models import Poem

class PoemForm(forms.ModelForm):
    class Meta:
        model=Poem
        #experiment with exclude=['slug'] 
        fields = '__all__' 

