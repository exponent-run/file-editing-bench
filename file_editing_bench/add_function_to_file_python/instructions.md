# Add Helper Function for Price Calculation

## Task Description
Add a helper function called `calculate_discounted_price` to the `order_processor.py` file and refactor the `process_order` method to use this helper function. The helper function should handle the price calculation and discount logic for individual order items.

## Specific Requirements

1. Add the following helper function to the `OrderProcessor` class:
```python
def calculate_discounted_price(self, item: OrderItem) -> float:
    """
    Calculate the total price for an item including any applicable discounts.
    
    Args:
        item: The OrderItem to calculate the price for
        
    Returns:
        float: The final price after applying any discounts
        
    Raises:
        ValueError: If quantity or unit_price is invalid
    """
    if item.quantity <= 0:
        raise ValueError(f"Invalid quantity for product {item.product_id}")
    if item.unit_price <= 0:
        raise ValueError(f"Invalid price for product {item.product_id}")
    
    item_price = item.quantity * item.unit_price
    
    # Apply category-specific discounts
    if item.category == "electronics":
        if item.quantity >= 3:
            item_price *= 0.85  # 15% bulk discount
    elif item.category == "books":
        if item.quantity >= 5:
            item_price *= 0.90  # 10% bulk discount
    elif item.category == "clothing":
        if datetime.now().month == 12:  # Holiday season
            item_price *= 0.95  # 5% seasonal discount
    
    return item_price
```

2. Refactor the `process_order` method to use this helper function instead of containing the price calculation logic directly.

## Success Criteria
- The helper function must be added exactly as specified above
- The `process_order` method must be refactored to use the helper function
- All existing functionality must remain the same
- All tests must pass

## Notes
- The helper function encapsulates the price calculation and discount logic that was previously in the `process_order` method
- The function should be added as a method within the `OrderProcessor` class
- The original validation and order storage logic should remain in the `process_order` method