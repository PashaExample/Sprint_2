import pytest
from main import BooksCollector


@pytest.fixture
# (scope='function') - тут по умолчанию поэтому не писал в параметрах
def collector():
    return BooksCollector()
