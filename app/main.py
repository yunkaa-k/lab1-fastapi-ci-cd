from fastapi import FastAPI, HTTPException, Response, status

from app.models import Item, ItemInput
from app.repository import ItemRepository

app = FastAPI(
    title="Items REST API",
    description="Basic CRUD web service for CI/CD laboratory work #1.",
    version="1.0.0",
)
repository = ItemRepository()


@app.get("/api/items", response_model=list[Item])
def list_items() -> list[Item]:
    return repository.list()


@app.get("/api/items/{item_id}", response_model=Item)
def get_item(item_id: int) -> Item:
    item = repository.get(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.post("/api/items", response_model=Item, status_code=status.HTTP_201_CREATED)
def create_item(data: ItemInput, response: Response) -> Item:
    item = repository.create(data)
    response.headers["Location"] = f"/api/items/{item.id}"
    return item


@app.put("/api/items/{item_id}", response_model=Item)
def update_item(item_id: int, data: ItemInput) -> Item:
    item = repository.update(item_id, data)
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.delete("/api/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item(item_id: int) -> None:
    if not repository.delete(item_id):
        raise HTTPException(status_code=404, detail="Item not found")

# Testing GitHub Actions feature branch