from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import (
    TemplateView,
    ListView,
    FormView,
    DetailView,
)
from django.contrib import messages
from .models import MenuItem
from order import forms
from order import models


# Create your views here.
class MenuHomeView(TemplateView):
    template_name = "menu/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active_page"] = "home"
        return context


class ItemListView(ListView):
    model = MenuItem
    context_object_name = "items"
    template_name = "menu/item_list.html"

    def get_queryset(self):
        return super().get_queryset().order_by("category", "price")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["active_page"] = "item_list"
        return context


class ItemDetailView(FormView, DetailView):
    model = MenuItem
    form_class = forms.OrderItemCreationForm
    template_name = "menu/item_detail.html"
    context_object_name = "item"
    # success_url = reverse_lazy('menu:item_detail')

    def post(self, request, *args, **kwargs):
        menu_item = self.get_object()
        order_item_model = models.OrderItem

        try:
            quantity = int(request.POST.get("quantity"))

            if quantity < 1:
                raise ValueError("Quantity must be at least 1")
            size_item = request.POST.get("size")
            if not size_item:
                raise ValueError("Please choose a size")
        except ValueError as e:
            print(e)
            return redirect(reverse("menu:item_detail", kwargs={"pk": menu_item.pk}))

        size = models.Size.objects.get(pk=size_item)
        new_order = order_item_model.objects.create(
            menu_item=menu_item,
            quantity=quantity,
            size=size,
        )
        print(new_order)

        return redirect(reverse("menu:item_list"))
