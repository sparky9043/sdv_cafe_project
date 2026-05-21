from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
from .models import OrderItem


class OrderItemListView(ListView):
    model = OrderItem
    template_name = "order/order_item_list.html"
    context_object_name = "order_items"
