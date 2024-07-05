from fastapi import FastAPI
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


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=FASTAPI_HOST, port=FASTAPI_PORT)
