# Function to validate the amount data.

def validate_amount(amount) -> tuple:
    try:
        a = float(amount)
    except (TypeError, ValueError):
        return False, "Amount must be a float"
    
    if a < 0:
        return False, "Amount must be greater than 0"
    return True, ""

# Function to validate the taxes data.

def validate_taxes(tax) -> tuple:
    try:
        t = float(tax)
    except (TypeError, ValueError):
        return False, "The tax must be a float"
    if not (0 <= t < 1):
        return False, "The taxes must be a number between 0 and 1"
    return True, ""
