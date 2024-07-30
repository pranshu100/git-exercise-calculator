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

def power_function(a,b):
    url = f'http://{FASTAPI_HOST}:{FASTAPI_PORT}/power'
    response = requests.post(url, json={'num1': a, 'num2': b})
    return response.json().get('result')
    

def log_function(a, b):
    url = f'http://{FASTAPI_HOST}:{FASTAPI_PORT}/log'
    response = requests.post(url, json={'num1': a, 'num2': b})
    return response.json().get('result')


def multi_sum_div(a,b):
    return a*b + a/b
