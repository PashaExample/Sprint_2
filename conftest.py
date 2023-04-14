import pytest

from main import BooksCollector


@pytest.fixture
def books_collector():
    return BooksCollector()


@pytest.fixture
def book1():
    return "Book 1"


@pytest.fixture
def book2():
    return "Book 2"