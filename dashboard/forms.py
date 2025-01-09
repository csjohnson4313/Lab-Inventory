from django import forms
from .models import Product, CustomOrderItem

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['package','name','category','quantity','location']

from .models import CustomOrderItem

class CustomOrderItemForm(forms.ModelForm):
    class Meta:
        model = CustomOrderItem
        fields = ['name', 'category', 'quantity', 'notes']
