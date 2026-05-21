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
