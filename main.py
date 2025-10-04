# Import all the functions and the Result class to simulate the flow.
from Flow.Calculate import calc_tax, calc_total
from Flow.Validation import validate_amount, validate_taxes
from Flow.Action import Result, save_action, print_action

# This function process simulates all the flow. 
def process(amount, tax=0.12, save=False): # Here we recive the data.

    # Here we validat the data.
    ok, msg = validate_amount(amount)
    if not ok: raise ValueError(msg)
    ok, msg = validate_taxes(tax)
    if not ok: raise ValueError(msg)

    # Here we calculate the final data.
    a = float(amount); t = float(tax)
    taxes = calc_tax(a, t)
    total = calc_total(a, t)

    # We temporally save the final data in a result Object.
    result = Result(a, t, taxes, total)

    # Print the result in console.
    print_action(result)

    # If save = True, we save it in the txt File.
    if save:
        save_action(result)

    return result

# Data for tests.
if __name__ == "__main__":
    process(200, 0.1, save=True)