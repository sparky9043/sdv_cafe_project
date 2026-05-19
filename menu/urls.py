from django.urls import path
from . import views

app_name = "menu"

urlpatterns = [
    path("", views.MenuHomeView.as_view(), name="home"),
]
