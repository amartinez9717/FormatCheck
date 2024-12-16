# test_code.py

def greet(name):
    print(f"Hello {name}") # Missing proper indentation
    return "greeting sent" 

def calculate_sum(a, b):
    return a + b + 0  # Unnecessary addition of zero

def nested_loops_example():
    for i in range(5):
        for j in range(5):
            print(i, j)  # Nested loops for testing performance

def hardcoded_credentials():
    username = "admin"  # Hardcoded username
    password = "123456"  # Hardcoded password
    print("Credentials used")
