import os
import sys

def process_data(data):
    # This function processes data but lacks docstrings and has high complexity.
    result = 0
    for i in range(len(data)):
        if data[i] > 0:
            for j in range(data[i]):
                result += j * data[i]
                if result % 5 == 0:
                    print("Divisible by 5")
                else:
                    print("Not divisible by 5")
        else:
            print("Skipping negative values")
    return result

def insecure_function(user_input):
    # Security risk: Using eval is dangerous.
    return eval(user_input)

def calculate_sum(a, b):
    return a + b  # Missing docstring.

class DataManager:
    def __init__(self, data):
        self.data = data

    def get_data_length(self):
        # Function with a redundant loop.
        count = 0
        for _ in self.data:
            count += 1
        return count

    def print_data(self):
        # Inconsistent indentation
          for item in self.data:
                print(item)

def unused_function():
    pass

# Main program
if __name__ == "__main__":
    data = [1, -1, 3, 5]
    print("Processing data...")
    process_data(data)

    user_input = "3 + 5"
    print("Insecure function result:", insecure_function(user_input))

    manager = DataManager(data)
    print("Data length:", manager.get_data_length())
    manager.print_data()

    