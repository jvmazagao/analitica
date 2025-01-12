from typing import Union
from fastapi import FastAPI

from app.processor.processor import Processor

app = FastAPI()

@app.get("/")
def reat_root():
    return {"message": "Hello World"}

@app.get("/stocks/{stock_id}")
def read_item(stock_id: str):
    extractor_process = Processor()
    stock = extractor_process.get_data(stock_id)
    return { **stock }