# Question 1 - Functions and Conditionals
# Topic: Temperature Converter
#
# Task 1:
# Write a function called convertTemp that accepts two arguments:
#   - value: a numeric temperature value
#   - unit: a string, either "C" for Celsius or "F" for Fahrenheit
#
# The function should:
#   - Convert Celsius to Fahrenheit if unit is "C"  →  Formula: (value × 9/5) + 32
#   - Convert Fahrenheit to Celsius if unit is "F"  →  Formula: (value − 32) × 5/9
#   - Return -1 if unit is neither "C" nor "F"
#   - Round the result to 2 decimal places before returning

def convertTemp(value, unit):
    unit = unit.strip().upper()

    if unit != "C" and unit != "F":
        return -1

    if not isinstance(value, (int, float)):
        return -1

    if unit == "C":
        return round((value * 9 / 5) + 32, 2)
    else:
        return round((value - 32) * 5 / 9, 2)
    


# Task 2:
# Call the function with the following inputs and print each result:
#   convertTemp(100, "C")     → Expected: 212.0
#   convertTemp(32, "F")      → Expected: 0.0
#   convertTemp(37, "C")      → Expected: 98.6
#   convertTemp("invalid","X")→ Expected: -1

print(convertTemp(100, "C"))       # Expected: 212.0
print(convertTemp(32, "F"))        # Expected: 0.0
print(convertTemp(37, "C"))        # Expected: 98.6
print(convertTemp("invalid", "X")) # Expected: -1
