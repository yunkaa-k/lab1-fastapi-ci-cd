from app.models import ItemInput
from app.repository import ItemRepository


def test_create_and_get():
    repo = ItemRepository()
    item = repo.create(ItemInput(name="Book", description="Python book"))
    assert item.id == 1
    assert repo.get(1) == item
    assert len(repo.list()) == 1


def test_update_existing_item():
    repo = ItemRepository()
    repo.create(ItemInput(name="Before"))
    updated = repo.update(1, ItemInput(name="After"))
    assert updated is not None
    assert updated.name == "After"
    assert repo.get(1).name == "After"


def test_update_missing_item():
    repo = ItemRepository()
    assert repo.update(999, ItemInput(name="Missing")) is None


def test_delete_and_missing_item():
    repo = ItemRepository()
    repo.create(ItemInput(name="Disposable"))
    assert repo.delete(1) is True
    assert repo.delete(1) is False
    assert repo.get(1) is None


def test_clear_resets_ids():
    repo = ItemRepository()
    repo.create(ItemInput(name="First"))
    repo.clear()
    assert repo.list() == []
    assert repo.create(ItemInput(name="Again")).id == 1
