

## Flow/Calculate.py
def calc_tax(amount, tax):
    return amount * tax

def calc_total(amount, tax):
    return amount + calc_tax(amount, tax)

## Flow/Validation.py
def validate_amount(amount):
    if amount <= 0:
        return False, "Amount must be greater than 0"
    return True, ""

def validate_taxes(tax):
    if tax < 0 or tax > 1:
        return False, "The taxes must be a number between 0 and 1"
    return True, ""

## Flow/Action.py
from dataclasses import dataclass

@dataclass
class Result:
    amount: float
    tax: float
    taxes: float
    total: float

def print_action(result: Result):
    print(result)

def save_action(result: Result, path="result.txt"):
    with open(path, "a", encoding="utf-8") as t:
        t.write(f"{result}\n") 

## main.py
from Flow.Calculate import calc_tax, calc_total
from Flow.Validation import validate_amount, validate_taxes
from Flow.Action import Result, save_action, print_action

def process(amount, tax=0.12, save=False):
    ok, msg = validate_amount(amount)
    if not ok: raise ValueError(msg)
    ok, msg = validate_taxes(tax)
    if not ok: raise ValueError(msg)

    taxes = calc_tax(amount, tax)
    total = calc_total(amount, tax)
    result = Result(amount, tax, taxes, total)

    print_action(result)
    if save:
        save_action(result)
    return result

if __name__ == "__main__":
    process(200, 0.1, save=True)

## tests/Calculate_test.py
import pytest
from Flow.Calculate import calc_tax, calc_total

def test_calc_tax():
    assert calc_tax(100, 0.1) == 10
    assert calc_tax(200, 0.2) == 40
    assert calc_tax(0, 0.1) == 0

def test_calc_total():
    assert calc_total(100, 0.1) == 110
    assert calc_total(200, 0.2) == 240
    assert calc_total(0, 0.1) == 0

## tests/integration/full_flow_test.py
import pytest
from main import process, Result

def test_full_flow(monkeypatch):
    printed = []
    monkeypatch.setattr("builtins.print", lambda x: printed.append(x))
    result = process(200, 0.1, save=False)
    assert isinstance(result, Result)
    assert result.amount == 200
    assert result.tax == 0.1
    assert result.taxes == 20
    assert result.total == 220
    assert str(result) in [str(p) for p in printed]

def test_invalid_amount():
    with pytest.raises(ValueError) as excinfo:
        process(-10, 0.1, save=False)
    assert "Amount must be greater than 0" in str(excinfo.value)

def test_invalid_tax():
    with pytest.raises(ValueError) as excinfo:
        process(100, 2.0, save=False)
    assert "The taxes must be a number between 0 and 1" in str(excinfo.value)

## README.md
# Software Engineering Flow Project

## Description
This project simulates a basic data flow using Python, consisting of three main modules:
1. Calculation (`Calculate`) – computes taxes and totals.
2. Validation (`Validation`) – validates input amounts and tax rates.
3. Action (`Action`) – prints results and optionally saves them to a file.

The `process` function orchestrates the entire flow: validation → calculation → action.

## Installation
Clone the repo:
```bash
git clone https://github.com/yourusername/Software_Engineering_Repo.git
cd Software_Engineering_Repo
