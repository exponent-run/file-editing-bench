def calculate_loyalty_points(purchase_amount, membership_years):
    """Calculate loyalty points for a customer based on purchase amount and membership years."""
    points = _apply_membership_multiplier(purchase_amount * 10, membership_years)
    
    if points > 10000:
        points *= 1.1  # bonus for high spenders
    
    return int(points)

def _apply_membership_multiplier(base_points, years):
    """Helper function to apply membership year multiplier to points."""
    if years <= 1:
        return base_points
    elif years <= 5:
        return base_points * 1.2
    else:
        return base_points * 1.5