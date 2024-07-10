# Enter your code for the calculator app
import math

import requests
FASTAPI_HOST='127.0.0.1'
FASTAPI_PORT='8000'

def add_function(a,b):
    url = f'http://{FASTAPI_HOST}:{FASTAPI_PORT}/sum'
    response = requests.post(url, json={'num1': a, 'num2': b})
    return response.json().get('result')

def mult_function(a,b):
    url = f'http://{FASTAPI_HOST}:{FASTAPI_PORT}/multiplication'
    response = requests.post(url, json={'num1': a, 'num2': b})
    return response.json().get('result')

    

def sub_function(a,b):
    url = f'http://{FASTAPI_HOST}:{FASTAPI_PORT}/sub'
    response = requests.post(url, json={'num1': a, 'num2': b})
    return response.json().get('result')
    

def div_function(a,b):
    url = f'http://{FASTAPI_HOST}:{FASTAPI_PORT}/div'
    response = requests.post(url, json={'num1': a, 'num2': b})
    return response.json().get('result')

def power_func(a,b):
    return pow(a,b)

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

def multi_sum_div(a,b):
    return a*b + a/b
