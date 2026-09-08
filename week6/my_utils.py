# my_utils.py (Custom Module for Lab 6.2)
# ============================================================
# This is a custom module containing utility functions.
# ============================================================

def greet(name):
    """Prints a greeting message to the given name."""
    print(f"Hello, {name}!")

def is_prime(number):
    """Returns True if the number is prime, False otherwise."""
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True
