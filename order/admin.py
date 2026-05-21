from django.contrib import admin
from .models import (
    OrderItem,
    Size,
    OrderSummary,
)

# Register your models here.
admin.site.register(OrderItem)
admin.site.register(OrderSummary)
admin.site.register(Size)
