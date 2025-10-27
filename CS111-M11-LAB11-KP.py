"""
Project/File Name: CS 111 Module 11 - Lab 11: Custom Module Demo
Author:           Kevin Pavione
Date Created:     October 22, 2025
Last Modified:    N/A

Purpose:          To demonstrate importing and using the custom Mathtools module
Dependencies:     Mathtools.py
Usage:            Run this file directly to test module features
"""

# Import entire module
import Mathtools

# Import specific functions and classes
from Mathtools import add, multiply, power, Calculator, AdvancedCalculator

def main():
    print("----- Testing Custom Module: MATHTOOLS Demo -----\n")

    # Using imported functions
    print("Using module functions:\n")
    print(f" add(5, 3) = {Mathtools.add(5, 3)}")
    print(f" multiply(4, 4) = {multiply(4, 4)}")
    print(f" power(2, 2) = {power(2, 2)}")
    print(f" subtract(10, 4) = {Mathtools.subtract(10, 4)}")
    print(f" divide(9, 3) = {Mathtools.divide(9, 3)}\n")

    # Using the Calculator class
    print("Using Calculator class:\n")
    calc = Calculator("DemoCalc")
    print(f" Calculator Name: {calc.name}")
    calc.calculate(add, 10, 5)
    calc.calculate(multiply, 3, 4)

    # Print history
    print("\nCalculation History:")
    for entry in calc.history:
        print(f" - {entry}")

    # Using the AdvancedCalculator class
    print("\nUsing AdvancedCalculator class:\n")
    adv_calc = AdvancedCalculator("SmartCalc")
    print(f" Calculator Name: {adv_calc.name}")
    print(f" factorial(5) = {adv_calc.factorial(5)}")
    print(f" average([2, 4, 6, 8]) = {adv_calc.average([2, 4, 6, 8])}")

    # Show history
    print("\nAdvanced Calculator History:")
    for entry in adv_calc.history:
        print(f" - {entry}")

if __name__ == "__main__":
    main()
