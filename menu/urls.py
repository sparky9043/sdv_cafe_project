from django.urls import path
from . import views

app_name = "menu"

urlpatterns = [
    path("", views.MenuHomeView.as_view(), name="home"),
    path("menu/", views.ItemListView.as_view(), name="item_list"),
    path("menu/<int:pk>/", views.ItemDetailView.as_view(), name="item_detail"),
]
