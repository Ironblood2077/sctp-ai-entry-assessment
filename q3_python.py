# Question 3 - String Manipulation
# Topic: Name Formatting Utility
#
# Task 1:
# Write a function called formatName(firstName, lastName) that accepts two strings
# and returns a formatted string in this format: "lastName, firstName"
# Example: formatName("John", "Smith") → "Smith, John"

def formatName(firstName, lastName):
    firstName = firstName.strip()
    lastName = lastName.strip()

    if firstName == "" or lastName == "":
        return "Invalid name"

    return lastName.capitalize() + ", " + firstName.capitalize()
    pass


# Task 2:
# Write a function called formatInitials(firstName, lastName) that returns the
# initials of the person as a string in uppercase.
# Example: formatInitials("john", "smith") → "J.S."
# Note: your function should handle inputs in any case (upper, lower, or mixed)
# and always produce properly capitalised output.

def formatInitials(firstName, lastName):
    firstName = firstName.strip()
    lastName = lastName.strip()

    if firstName == "" or lastName == "":
        return "Invalid name"

    return firstName[0].upper() + "." + lastName[0].upper() + "."
    pass


# Task 3:
# Call both functions with the following inputs and print each result:
#   formatName("Alice", "Tan")  → Expected: "Tan, Alice"
#   formatName("bob", "lim")    → Expected: "Lim, Bob"
#   formatInitials("Alice","Tan") → Expected: "A.T."
#   formatInitials("bob","lim")   → Expected: "B.L."

print(formatName("Alice", "Tan"))          # Expected: Tan, Alice
print(formatName("bob", "lim"))            # Expected: Lim, Bob
print(formatInitials("Alice", "Tan"))      # Expected: A.T.
print(formatInitials("bob", "lim"))        # Expected: B.L.


