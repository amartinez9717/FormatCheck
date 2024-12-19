import os
import math  # Unused import
import json

# Global variable with improper naming
my_var = 42

# Function missing a docstring
def example_function_1(x, y):
    a = x + y
    b = x - y
    c = x * y
    d = x / y
    return a, b, c, d

# Function too long (pylint, cyclomatic complexity issues)
def long_function_with_high_complexity(n):
    # No docstring
    if n > 0:
        if n % 2 == 0:
            for i in range(n):
                if i % 3 == 0:
                    print(f"Divisible by 3: {i}")
                else:
                    print(f"Not divisible by 3: {i}")
        else:
            while n > 0:
                n -= 1
                if n == 5:
                    print("N is five")
    else:
        print("N is zero or negative")
    return n

# Class too large and missing a docstring
class ExampleClass:
    def __init__(self):
        self.data = []

    def add(self, item):
        self.data.append(item)

    def remove(self, item):
        if item in self.data:
            self.data.remove(item)

    def print_all(self):
        for item in self.data:
            print(item)

    def clear(self):
        self.data = []

    def save(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.data, f)

    def load(self, filename):
        with open(filename, 'r') as f:
            self.data = json.load(f)

# Function with unused variables
def example_function_2():
    unused_variable = 123
    another_unused = "Hello"
    print("This function does something minimal.")
    