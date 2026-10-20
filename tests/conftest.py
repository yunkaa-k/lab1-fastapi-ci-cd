import pytest

from app.main import repository


@pytest.fixture(autouse=True)
def fresh_api_data():
    repository.clear()
    yield
    repository.clear()
