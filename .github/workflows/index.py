# Example file to demonstrate issues detected by pylint, flake8, radon, and custom AST analysis

import os  # Unused import (flake8, pylint)

def process_data(data):
    """Function to process data - docstring included to avoid missing-docstring warnings."""
    result = []
    for i in range(len(data)):  # Using range(len()) is a common anti-pattern (pylint, flake8)
        result.append(data[i] * 2)
    return result

def another_function(data, value): # Missing whitespace around the operator (flake8)
    return [x+value for x in data] # No spaces around operators (flake8)

class LargeClass:  # Large class to trigger AST-based code smell analysis
    def __init__(self):
        self.data = [i for i in range(100)]

    def method_one(self):
        pass

    # Add many methods to simulate a large class
    def method_two(self): pass
    def method_three(self): pass
    def method_four(self): pass
    def method_five(self): pass
    def method_six(self): pass
    def method_seven(self): pass
    def method_eight(self): pass
    def method_nine(self): pass
    def method_ten(self): pass
    def method_eleven(self): pass
    def method_twelve(self): pass
    def method_thirteen(self): pass
    def method_fourteen(self): pass
    def method_fifteen(self): pass

def complex_function(a, b, c):
    """Complex function to trigger cyclomatic complexity analysis."""
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

def very_large_function(data):  # Long function to trigger AST-based "too large function" analysis
    """This function has too many lines to demonstrate a code smell."""
    total = 0
    for i in range(10):  # Arbitrary loop to increase function size
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

# Missing module-level docstring (pylint)
