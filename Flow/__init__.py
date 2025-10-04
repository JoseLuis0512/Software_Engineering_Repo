# Flow/__init__.py
# This file makes the Flow folder a Python package
# and exposes main functions and classes for easy import

# Import calculation functions
from .Calculate import calc_tax, calc_total

# Import validation functions
from .Validation import validate_amount, validate_taxes

# Import action functions and Result dataclass
from .Action import Result, print_action, save_action
