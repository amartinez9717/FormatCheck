import os  # Unused import

# Function with high cyclomatic complexity
def complex_function(a, b, c):
    if a > b:
        if b > c:
            return a + b + c
        elif b == c:
            return a - b - c
        else:
            return a * b * c
    else:
        if a == c:
            return a
        elif a < b:
            return b
        else:
            return c

# Missing docstring (Pylint will flag this)
def add(x, y):
    return x + y

# Function with too many nested conditions (DeepCode warning for complexity)
def deep_code_issue(x):
    if x > 10:
        if x < 20:
            if x == 15:
                return "Very Specific"
            else:
                return "Between 10 and 20"
        else:
            return "Greater than 20"
    else:
        return "Smaller than 10"

# Function with a multiple statements in one line (Flake8 warning)
def multiple_statements_in_one_line():
    a = 10; b = 20  # Multiple statements in one line (Flake8 warning)
    return a + b

# Function with unused variable (DeepCode warning)
def unused_variable(x):
    y = x * 2  # Unused variable y
    return x

# Docstring issues (Docformatter will flag this)
def function_with_inconsistent_docstring():
    """This is a poorly formatted docstring
    that should be fixed."""
    return "Hello, World!"

# Security vulnerability (Snyk will detect this if you use an outdated library like 'requests' with known vulnerabilities)
import requests

def security_vulnerable_function():
    response = requests.get('https://example.com')
    return response.content

# A simple function with poor variable names (Pylint will flag this)
def f(x, y):
    z = x + y
    return z

# Function with missing blank lines (Flake8 will flag this)
def missing_blank_lines():
    x = 10
    y = 20
    return x + y