from django import forms
from .models import Product, CustomOrderItem
from .models import EquipmentCheckout
from .models import CustomOrderItem

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['package','name','category','quantity','location','link']


class CustomOrderItemForm(forms.ModelForm):
    class Meta:
        model = CustomOrderItem
        fields = ['package','name', 'category', 'quantity', 'notes']


class EquipmentCheckoutForm(forms.ModelForm):
    class Meta:
        model = EquipmentCheckout
        fields = ['equipment', 'user', 'location']
