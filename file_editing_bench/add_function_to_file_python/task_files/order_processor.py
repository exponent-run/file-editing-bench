from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime


@dataclass
class OrderItem:
    product_id: str
    quantity: int
    unit_price: float
    category: str


@dataclass
class Order:
    order_id: str
    customer_id: str
    items: List[OrderItem]
    created_at: datetime
    special_instructions: Optional[str] = None


class OrderProcessor:
    def __init__(self):
        self.orders: List[Order] = []
    
    def process_order(self, order: Order) -> float:
        """Process an order and return the total price."""
        if not order.items:
            raise ValueError("Order must contain at least one item")
        
        total_price = 0.0
        for item in order.items:
            # Basic validation
            if item.quantity <= 0:
                raise ValueError(f"Invalid quantity for product {item.product_id}")
            if item.unit_price <= 0:
                raise ValueError(f"Invalid price for product {item.product_id}")
            
            # Calculate item total
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
            
            total_price += item_price
        
        # Store the processed order
        self.orders.append(order)
        return round(total_price, 2)

    def get_order_history(self, customer_id: str) -> List[Order]:
        """Retrieve order history for a customer."""
        return [order for order in self.orders if order.customer_id == customer_id]