from dataclasses import dataclass # Use to create a class without a lot of code.

# Python will automatically generate the class.
@dataclass
class Result:
    amount: float
    tax: float
    taxes: float
    total: float

# Fucntion to print the result in console.
def print_action(result: Result):
    print(result)

# Function to save the result in a ".txt" file
def save_action(result: Result, path="result.txt"):
    with open(path, "a", encoding="utf-8") as t:
        t.write(f"{result}\n") 