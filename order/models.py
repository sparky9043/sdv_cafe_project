from django.db import models


class Size(models.Model):
    type = models.CharField(
        max_length=10,
        choices=[
            ("small", "small"),
            ("medium", "medium"),
            ("large", "large"),
        ],
    )

    def __str__(self):
        return self.type


# Create your models here.
class OrderItem(models.Model):
    menu_item = models.ForeignKey(
        "menu.MenuItem",
        related_name="order_items",
        on_delete=models.CASCADE,
    )
    quantity = models.IntegerField()
    size = models.ForeignKey(
        Size,
        related_name="order_items",
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return f"{self.quantity}x {self.size} - {self.menu_item.name}"

    def _get_price(self):
        surcharge = 0
        if self.size.type == "medium":
            surcharge += 0.50
        elif self.size.type == "large":
            surcharge += 1.00
        current_price = float(self.menu_item.price)
        return current_price + surcharge


class OrderSummary(models.Model):
    time_added = models.DateTimeField(auto_now_add=True)
    order_complete = models.BooleanField(default=False)
    order_items = models.ManyToManyField(
        OrderItem,
        related_name="orders",
    )

    def __str__(self):
        return f"Order #: {self.pk} | Completed: {self.order_complete}"
