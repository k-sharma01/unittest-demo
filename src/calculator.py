class Calculator:
    """Simple calculator class with basic operations."""

    # Returns the sum of two numbers a and b
    def add(self, a, b):
        return a + b

    # Returns the difference of two numbers a and b
    def subtract(self, a, b):
        return a - b

    # Returns the product of two numbers a and b
    def multiply(self, a, b):
        return a * b

    # Returns the quotient of two numbers a and b
    def divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return a / b
