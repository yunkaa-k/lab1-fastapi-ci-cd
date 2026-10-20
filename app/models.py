from pydantic import BaseModel, Field


class ItemInput(BaseModel):
    name: str = Field(min_length=1, max_length=120)
    description: str | None = None


class Item(ItemInput):
    id: int
