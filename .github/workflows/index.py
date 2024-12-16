# This module demonstrates code analysis features for static analysis and AST.

import os  # Unused import (flake8, pylint)

# Function with poor design to test static analysis tools
def process_data(data):
    """Processes data using an inefficient pattern."""
    result = []
    for i in range(len(data)):  # Using range(len()) is a common anti-pattern
        result.append(data[i] * 2)
    return result

def another_function(data, value): # Missing whitespace around the operator
    return [x+value for x in data] # No spaces around operators (flake8)

class LargeClass:  # A class intentionally designed to be large
    def __init__(self):
        self.data = [i for i in range(100)]

    def method_one(self):
        pass

    # Add multiple methods to simulate a large class
    def method_two(self): pass
    def method_three(self): pass
    def method_four(self): pass
    def method_five(self): pass
    def method_six(self): pass
    def method_seven(self): pass
    def method_eight(self): pass
    def method_nine(self): pass
    def method_ten(self): pass

def complex_function(a, b, c):
    """A complex function to demonstrate cyclomatic complexity."""
    if a > b:
        if b > c:
            return a
        else:
            return b
    elif b > c:
        if a > c:
            return b
        else:
            return c
    else:
        return c

# Very large function example for AST analysis
def very_large_function(data):
    """This function has too many lines."""
    total = 0
    for i in range(10):
        total += i
    for j in range(10):
        total += j
    for k in range(10):
        total += k
    for l in range(10):
        total += l
    for m in range(10):
        total += m
    return total
