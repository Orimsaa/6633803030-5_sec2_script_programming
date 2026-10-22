# ============================================================
# Lab 6.2: Custom Module and Standard Library Usage
# ------------------------------------------------------------
# Part 2: Use Custom Module + Standard Modules (math, random)
# ============================================================

# --- Importing custom module ---
import my_utils

# --- Importing standard library modules ---
import math
import random

# === ทดสอบ Custom Module ===
print("--- Testing Custom Module (my_utils) ---")
my_utils.greet("Alice")

test_numbers = [7, 10, 13, 20, 23]
for num in test_numbers:
    print(f"Is {num} prime? {my_utils.is_prime(num)}")

# === ทดสอบ math module ===
print("\n--- Testing math Module ---")
number_to_sqrt = 16
print(f"Square root of {number_to_sqrt} is {math.sqrt(number_to_sqrt)}")
print(f"Value of pi: {math.pi}")

# === ทดสอบ random module ===
print("\n--- Testing random Module ---")
random_num = random.randint(1, 100)
print(f"Random number between 1 and 100: {random_num}")
