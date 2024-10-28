from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Product(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    description = models.TextField(blank=True, help_text="Detailed product description")
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0), MaxValueValidator(999999.99)],
        help_text="Product price in USD",
    )
    sku = models.CharField(
        max_length=20,
        unique=True,
        help_text="Stock Keeping Unit - unique product identifier",
    )
    stock = models.PositiveIntegerField(default=0)
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
