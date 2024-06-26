# Enter your code for the calculator app
import math
def add_function(a,b):
    return a+b

def mult_function(a,b):
    return a*b

def sub_function(a,b):
    return a-b

def div_function(a,b):
    if b==0:
        raise ZeroDivisionError("Division by zero is undefined.")
    return a/b

def log_function(base, num):
    # Check if base is valid for logarithm calculation
    if base <= 0:
        return "Error: Base must be positive."
    if base == 1:
        return "Error: Base cannot be 1."
    # Check if num is valid for logarithm calculation
    if num <= 0:
        return "Error: Number must be positive."
    
    # Use math.log to calculate the logarithm with the specified base
    result = math.log(num, base)
    return result

