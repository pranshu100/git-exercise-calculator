# Enter your code for the calculator app

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

