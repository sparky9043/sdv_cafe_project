from django.urls import path
from . import views

app_name = "menu"

urlpatterns = [
    path("", views.MenuHomeView.as_view(), name="home"),
    path("items/", views.ItemListView.as_view(), name="item_list"),
]
