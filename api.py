from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
import os
app = FastAPI()
# from dotenv import load_dotenv

# # Load environment variables from .env file
# load_dotenv()

# # Access variables
# FASTAPI_HOST = os.getenv('FASTAPI_HOST')
# FASTAPI_PORT = os.getenv('FASTAPI_PORT')

FASTAPI_HOST='127.0.0.1'
FASTAPI_PORT='8000'


class Numbers(BaseModel):
    num1: float
    num2: float

@app.post("/sum")
async def add_function(numbers: Numbers):
    result = numbers.num1 + numbers.num2
    return {"result": result}

@app.post("/sub")
async def sub_function(numbers: Numbers):
    result = numbers.num1 - numbers.num2
    return {"result": result}

@app.post("/div")
async def div_function(numbers: Numbers):
    if numbers.num2==0:
        raise HTTPException(400,"Choose a divisor other than 0")

    result = numbers.num1 / numbers.num2
    return {"result": result}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=FASTAPI_HOST, port=FASTAPI_PORT)
