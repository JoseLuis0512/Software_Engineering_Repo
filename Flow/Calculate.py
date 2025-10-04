# Function to calculate taxes.

def calc_tax(amount: float, tax: float = 0.12) -> float:
    return round(amount * tax, 2)

# Function to calculate the total amount.
def calc_total(amount: float, tax: float = 0.12) -> float:
    return round(amount + calc_tax(amount, tax), 2)