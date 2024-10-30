def process_customer_purchase(customer_name, years_as_customer, purchase_amount):
    """Process a customer purchase and apply appropriate discounts"""
    if not isinstance(purchase_amount, (int, float)) or purchase_amount <= 0:
        raise ValueError("Purchase amount must be a positive number")
    
    # Helper function to calculate a customer's discount multiplier based on loyalty
    base_multiplier = 0.95  # 5% base discount
    loyalty_bonus = min(years_as_customer * 0.01, 0.15)  # Up to 15% loyalty bonus
    volume_bonus = 0.05 if purchase_amount > 1000 else 0
    multiplier = base_multiplier - loyalty_bonus - volume_bonus
    
    final_price = purchase_amount * multiplier
    
    return {
        "customer": customer_name,
        "original_amount": purchase_amount,
        "final_price": round(final_price, 2),
        "savings": round(purchase_amount - final_price, 2)
    }
