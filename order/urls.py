from django.urls import path
from .views import (
    OrderItemListView,
)

app_name = "order"

urlpatterns = [
    path("cart/", OrderItemListView.as_view(), name="order_item_list"),
]
