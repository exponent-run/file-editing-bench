from django.db import models
from django.core.validators import MinValueValidator


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(0)]
    )
    sku = models.CharField(max_length=20, unique=True)
    stock = models.IntegerField(default=0)
    category = models.ForeignKey(
        "Category", on_delete=models.PROTECT, related_name="products"
    )

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["sku"]),
        ]

    def __str__(self):
        return f"{self.name} ({self.sku})"

    def is_in_stock(self):
        return self.stock > 0
