# Enter your code for the calculator ap
# adding 
def add_function(a,b):
    return a+b


def mult_function(a,b):
    return a*b

def div_function(a,b):
    if b==0:
        raise ZeroDivisionError("Division by zero is undefined.")
    return a/b