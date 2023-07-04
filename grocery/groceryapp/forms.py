from django import forms
from .models import Grocery

class GroceryForm(forms.ModelForm):
    class Meta:
        model = Grocery
        fields = '__all__'
        lables = {
            'groceryitems':forms.CharField(max_length=50),
            'price':forms.FloatField(),
            'date' : forms.DateField(widget=forms.DateField)
        }