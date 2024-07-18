import pytest
from test_main import BooksCollector


@pytest.fixture
def book():
    book = BooksCollector()
    return book
