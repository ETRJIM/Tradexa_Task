from django import forms
from Products.models import Product

class ProductForm(forms.ModelForm):
    weight = forms.DecimalField(),
    price = forms.DecimalField(),
    
    class Meta():
        model = Product
        fields = ('name','weight','price')

        widgets = {
            'name':forms.TextInput(),    
        }