from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import MenuItem


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
