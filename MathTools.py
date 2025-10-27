"""
Project/File Name: CS 111 Module 11 - Lab 11: Custom Module Demo
Author:           Kevin Pavione
Date Created:     October 22, 2025
Last Modified:    N/A

Purpose:          To showcase workings of custom modules in Python

Dependencies:     None
Usage:            Import into another Python file to use mathematical functions and classes
Inputs:           Function parameters (numbers, lists)
Outputs:          Calculated results or stored history
Notes:            Example module for demonstration purposes
"""

"""
A simple module for mathematical operations.
This demo shows how to create and use custom modules within Python.
"""

# ------------------------------
# Basic Mathematical Functions
# ------------------------------

def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


def power(base, exponent):
    """Return the base raised to the given exponent."""
    return base ** exponent


def subtract(a, b):
    """Return the difference of two numbers."""
    return a - b


def divide(a, b):
    """Safely divide two numbers."""
    if b == 0:
        return "Error: Division by zero is undefined."
    return a / b


# ------------------------------
# Calculator Classes
# ------------------------------

class Calculator:
    """A simple calculator class that performs basic operations."""

    def __init__(self, name="MyCalculator"):
        self.name = name
        self.history = []

    def calculate(self, operation, a, b):
        """Perform a calculation and store it in history."""
        result = operation(a, b)
        self.history.append(f"{operation.__name__}({a}, {b}) = {result}")
        return result

    def clear_history(self):
        """Clear calculation history."""
        self.history = []
        return "Calculation history cleared."


class AdvancedCalculator(Calculator):
    """An advanced calculator with extra mathematical functions."""

    def __init__(self, name="AdvancedCalculator"):
        super().__init__(name)

    def factorial(self, n):
        """Compute factorial of n."""
        if n < 0:
            return "Error: Factorial not defined for negative numbers."
        result = 1
        for i in range(1, n + 1):
            result *= i
        self.history.append(f"factorial({n}) = {result}")
        return result

    def average(self, numbers):
        """Compute average of a list of numbers."""
        if not numbers:
            return "Error: Cannot calculate average of an empty list."
        result = sum(numbers) / len(numbers)
        self.history.append(f"average({numbers}) = {result}")
        return result


