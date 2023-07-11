from django import forms
from .models import Grocery

class GroceryForm(forms.ModelForm):
    class Meta:
        Discounts = forms.CharField(label='2%')
        model = Grocery
        fields = ['groceryitems', 'price', 'date']
        widgets = {
            'groceryitems':forms.TextInput(),
            'date' :forms.DateInput(attrs={'type': 'date'})
        }
