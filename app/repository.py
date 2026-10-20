from app.models import Item, ItemInput


class ItemRepository:
    def __init__(self) -> None:
        self._items: dict[int, Item] = {}
        self._next_id = 1

    def list(self) -> list[Item]:
        return list(self._items.values())

    def get(self, item_id: int) -> Item | None:
        return self._items.get(item_id)

    def create(self, data: ItemInput) -> Item:
        item = Item(id=self._next_id, **data.model_dump())
        self._items[item.id] = item
        self._next_id += 1
        return item

    def update(self, item_id: int, data: ItemInput) -> Item | None:
        if item_id not in self._items:
            return None
        item = Item(id=item_id, **data.model_dump())
        self._items[item_id] = item
        return item

    def delete(self, item_id: int) -> bool:
        return self._items.pop(item_id, None) is not None

    def clear(self) -> None:
        """Restore a blank repository (used by test fixtures)."""
        self._items.clear()
        self._next_id = 1
