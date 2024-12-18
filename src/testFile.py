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


def add(x, y): # Missing docstring (Pylint will flag this)
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
    z = x * 3  # Unused variable z
    return x

# Docstring issues (Docformatter will flag this)
def function_with_inconsistent_docstring():
    """This is a poorly formatted docstring
    that should be fixed."""
    return "Hello, World!"

# A simple function with poor variable names (Pylint will flag this)
def f(x, y):
    z = x + y
    return z

# Function with missing blank lines (Flake8 will flag this)
def missing_blank_lines():
    x = 10
    y = 20
    return x + y

# Security Vulnerability: Hardcoded secret
API_KEY = "12345-SECRET-KEY"

# Documentation Error: Missing or poorly formatted docstrings
def insecure_function(file_path):
  """
  Executes a shell command.
  The file_path parameter is not validated properly.
  """
  command = f"cat {file_path}"  # Command injection vulnerability
  subprocess.call(command, shell=True)  # Dangerous: Allows command injection


def unused_function():
  """
  This function is not used anywhere.
  """
  pass

# DeepCode Issue: Unused variable and improper exception handling
def calculate():
  try:
    result = 10 / 0  # This will raise a ZeroDivisionError
  except:
    print("Something went wrong!")  # Broad exception: hides details
    return None

  unused_variable = 42  # Unused variable

# Security Vulnerability: Use of insecure method (eval)
def dangerous_eval(user_input):
  """
  Evaluate user input directly without sanitization.
  """
  return eval(user_input)  # Potential code execution vulnerability

# Poorly formatted function
def  poorly_formatted_function ( ) :
  """
  This function has inconsistent spacing in its definition.
  """
  print("This is a poorly formatted function.")
