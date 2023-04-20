from main import BooksCollector
import pytest
import conftest


class TestBooksCollector:

    def test_add_new_book_add_two_books(self, books_collector):
        books_collector.add_book('Гордость и предубеждение и зомби')
        books_collector.add_book('Что делать, если ваш кот хочет вас убить')
        assert len(books_collector.get_books_rating()) == 2

    @pytest.mark.parametrize("rating, expected_result", [
        (5, ["Book 1"]),
        (3, ["Book 2"]),
        (1, [])
    ])
    def test_get_books_by_rating(self, books_collector, book1, book2, rating, expected_result):
        books_collector.add_book(book1)
        books_collector.add_book(book2)
        books_collector.set_book_rating(book1, 5)
        books_collector.set_book_rating(book2, 3)
        assert books_collector.get_books_by_rating(rating) == expected_result

    def test_add_same_book_to_favorites(self, books_collector, book1):
        books_collector.add_book(book1)
        books_collector.add_to_favorites(book1)
        books_collector.add_to_favorites(book1)
        assert len(books_collector.get_favorites()) == 1

    def test_add_book_with_empty_name(self, books_collector):
        books_collector.add_book("")
        assert books_collector.get_books_rating() == {"": 1}

    def test_add_book_with_special_characters(self, books_collector):
        book_name = "C++ Programming for Beginners [Special Edition]\n"
        books_collector.add_book(book_name)
        assert book_name in books_collector.get_books_rating()

    @pytest.mark.parametrize("book", ["Book 1", "Book 2"])

    def test_remove_book_that_does_not_exist(self, books_collector, book):
        books_collector.add_book(book)
        books_collector.delete_book_from_favorites(book)
        books_collector.set_book_rating(book, 5)
        assert books_collector.get_books_rating() == {book: 5}

    def test_set_book_rating(self, books_collector, book2):
        books_collector.add_book(book2)
        books_collector.set_book_rating(book2, 5)
        assert books_collector.get_book_rating(book2) is None

    def test_add_to_favorites(self, books_collector, book1, book2):
        books_collector.add_book(book1)
        books_collector.add_to_favorites(book1)
        assert book1 in books_collector.get_favorites()

    def test_delete_book_from_favorites(self, books_collector, book1):
        books_collector.add_book(book1)
        books_collector.add_to_favorites(book1)
        books_collector.delete_book_from_favorites(book1)
        assert book1 not in books_collector.get_favorites()

    @pytest.mark.parametrize("book_name, expected_result", [
        ("", {"": 1}),
        ("C++ Programming for Beginners [Special Edition]\n", {"C++ Programming for Beginners [Special Edition]\n": 1})
    ])
    def test_add_book_with_special_cases(self, books_collector, book_name, expected_result):
        books_collector.add_book(book_name)
        assert books_collector.get_books_rating() == expected_result

    def test_get_books_rating(self, books_collector, book1):
        books_collector.add_book(book1)
        books_collector.set_book_rating(book1, 5)
        assert books_collector.get_books_rating() == {book1: 5}
