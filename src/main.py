from fastapi import FastAPI

app = FastAPI()


# root
@app.get("/")
def home():
    return {"message":"Root page"}


# about me
@app.get("/me")
def say():
    return {"message": "About Delroy"}


# sending data
@app.post("/items")
def createshop():
    return {"message": "Items shop created"}


# get items
@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"message":f"Get item : {item_id}"}


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

