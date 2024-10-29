def calculate_loyalty_points(purchase_amount, membership_years):
    """Calculate loyalty points for a customer based on purchase amount and membership years."""
    # Helper function to apply membership year multiplier to points
    base_points = purchase_amount * 10
    if membership_years <= 1:
        points = base_points
    elif membership_years <= 5:
        points = base_points * 1.2
    else:
        points = base_points * 1.5
    
    if points > 10000:
        points *= 1.1  # bonus for high spenders
    
    return int(points)