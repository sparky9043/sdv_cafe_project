from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
from .models import OrderItem


class OrderItemListView(ListView):
    model = OrderItem
    template_name = "order/order_item_list.html"
    context_object_name = "order_items"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order_items: list[OrderItem] = list(context["order_items"])
        subtotal = sum(order._get_price() * order.quantity for order in order_items)
        tax_percent = 11
        tax_amount = subtotal * (tax_percent / 100)
        total_bill = f"{subtotal + tax_amount:.2f}"
        context["subtotal"] = f"{subtotal:.2f}"
        context["tax_percent"] = tax_percent
        context["tax_amount"] = f"{tax_amount:.2f}"
        context["total_bill"] = total_bill
        return context
