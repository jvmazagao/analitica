from fastapi import FastAPI

from processor.processor import Processor

api = FastAPI()

@api.get("/")
def read_root():
    return {"Hello": "World"}

@api.get("/stocks/{item_id}")
def read_item(item_id: str, q: str = None):
    processor = Processor()
    data = processor.get_data(item_id)
    return { **data }