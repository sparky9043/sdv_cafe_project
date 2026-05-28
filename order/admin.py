from django.contrib import admin
from .models import (
    OrderItem,
    Size,
    Cart,
)

# Register your models here.
admin.site.register(OrderItem)
admin.site.register(Cart)
admin.site.register(Size)
