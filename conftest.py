import pytest

from helpers import generate_random_book_title
from main import BooksCollector


@pytest.fixture
def collector():
    collector = BooksCollector()
    return collector

@pytest.fixture()
def collector_with_favorites(collector):
    collector.add_book_in_favorites(generate_random_book_title())
    return collector