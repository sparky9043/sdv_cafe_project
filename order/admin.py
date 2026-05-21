from django.contrib import admin
from .models import (
    OrderItem,
    Size,
)

# Register your models here.
admin.site.register(OrderItem)
admin.site.register(Size)
