from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
import os
from logger import logger
import math
app = FastAPI()
logger.info("Starting API...")


FASTAPI_HOST='127.0.0.1'
FASTAPI_PORT='8000'


class Numbers(BaseModel):
    num1: float
    num2: float



@app.post("/sum")
async def add_function(numbers: Numbers):
    result = numbers.num1 + numbers.num2
    logger.info(f"Added numbers {numbers.num1} and {numbers.num2}")
    return {"result": result}

@app.post("/multiplication")
async def mult_function(numbers: Numbers):
    result = numbers.num1 * numbers.num2
    logger.info(f"Multiplied numbers {numbers.num1} and {numbers.num2}")
    return {"result": result} 
  
  
@app.post("/sub")
async def sub_function(numbers: Numbers):
    result = numbers.num1 - numbers.num2
    logger.info(f"Subtracted two numbers numbers {numbers.num1} and {numbers.num2}")
    return {"result": result}

@app.post("/div")
async def div_function(numbers: Numbers):
    if numbers.num2==0:
        raise HTTPException(400,"Choose a divisor other than 0")

    result = numbers.num1 / numbers.num2
    return {"result": result}

@app.post("/power")
async def power_function(numbers: Numbers):
    if numbers.num1==0 and numbers.num2==0:
        logger.error('both numbers are 0')
        raise HTTPException(400,"Both numbers cant be 0, enter another number")

    result = pow(numbers.num1 , numbers.num2)
    logger.info(f"Power of {numbers.num1} raised to {numbers.num2}")
    logger.info("Both numbers are not zero")
    return {"result": result}

@app.post("/log")
async def power_function(numbers: Numbers):
    if numbers.num1 <= 0:
        logger.error('base is not positive')
        raise HTTPException(400,"Error: Base must be positive.")
         
    if numbers.num1 == 1:
        logger.error('base is 1')
        raise HTTPException(400,"Error: Base cannot be 1.") 
    # Check if num is valid for logarithm calculation
    if numbers.num2 <= 0:
        logger.error('Number is negative')
        raise HTTPException(400,"Error: Number must be positive.") 
    result = math.log(numbers.num1 , numbers.num2)
    logger.info(f"log of {numbers.num2} with base {numbers.num1}")
    logger.info("base is >0 and not equal to 1 also number is positive")
    return {"result": result}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=FASTAPI_HOST, port=FASTAPI_PORT)
