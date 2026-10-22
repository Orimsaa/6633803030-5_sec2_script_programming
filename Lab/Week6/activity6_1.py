# ============================================================
# Activity 6.1: Refactoring a Previous Lab Assignment
# ------------------------------------------------------------
# Refactored from Week 2 Lab 2.1 (Number Classifier)
# Original: inline if/elif logic
# Refactored: encapsulated into reusable functions
# ============================================================

def classify_sign(num):
    """Classifies a number as positive, negative, or zero."""
    if num > 0:
        return "positive"
    elif num < 0:
        return "negative"
    else:
        return "zero"

def classify_parity(num):
    """Classifies a number as even or odd."""
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

def classify_number(num):
    """Returns a formatted string describing the number's sign and parity."""
    sign = classify_sign(num)
    parity = classify_parity(num)
    return f"The number is {sign} and {parity}."


# === Main Program (refactored) ===
num = int(input("Enter an integer: "))
result = classify_number(num)
print(result)
