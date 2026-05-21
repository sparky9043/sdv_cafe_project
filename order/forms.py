from django import forms
from .models import OrderItem


class OrderItemCreationForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ["quantity", "size"]
