from fastapi import FastAPI

from processors.processor import Processor
from service.models.model import Stock

api = FastAPI()

@api.get("/")
def read_root():
    return {"Hello": "World"}

@api.get("/stocks/{item_id}")
async def read_item(item_id: str, q: str = None):
    processor = Processor()
    data: dict = processor.get_data(item_id)   
    res = Stock(**data) 
    return { "stock": res.model_dump() }