1. Edit the file `original_code.py` to modify the Product model fields with these exact changes:
   - Add `db_index=True` to the name field
   - Add help_text="Detailed product description" to the description field
   - Add MaxValueValidator(999999.99) to price field's validators and help_text="Product price in USD"
   - Add help_text="Stock Keeping Unit - unique product identifier" to the sku field
   - Change stock field from IntegerField to PositiveIntegerField
   - Import MaxValueValidator from django.core.validators alongside MinValueValidator