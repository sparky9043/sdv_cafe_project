from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    category = models.ForeignKey(
        Category,
        related_name="items",
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"[{self.category}] {self.name}"
