from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    instock: bool = True

item_list = []

# root
@app.get("/")
def home():
    return {"message":"Root page"}


# about me
@app.get("/me")
def say():
    return {"message": "About Delroy"}


# create items
@app.post("/items")
def create_item(item: Item):
    new_item = item.model_dump()
    new_item["id"] = len(item_list) + 1

    item_list.append(new_item)
    return {"message": "Item created", "item": item}


# get ONE items
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"message":f"Get item : {item_id}"}


# get ALL items
@app.get("/items")
def get_all_item():
    return {"items": item_list}

# Updating items
@app.put("/items/{item_id}")
def update_item(item_id : int):
    return {"message":f"Updating item :{item_id}"}


# partial updation of item
@app.patch("/items/{item_id}")
def update_partial(item_id : int):
    return {"message":f"Partially updated item: {item_id}"}

# delete an item
@app.delete("/items/{item_id}")
def delete_item(item_id : int):
    return {"message":f"Deletion of item {item_id} complete"}

