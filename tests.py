import pytest

book1 = 'Война и Мир'
book2 = 'Мастер и Маргарита'
books_with_ratings = {
    book1: 6,
    book2: 10,
    'От заката до рассвета': 8
}


class TestBooksCollector:

    def test_init_books_rating_type_is_dictionary(self, books_collector):
        assert books_collector.get_books_rating() == {}, 'Тип рейтинга книг не является словарным'

    def test_init_favorites_type_is_list(self, books_collector):
        assert books_collector.get_list_of_favorites_books() == [], 'Тип списка любимых книг - это не список'

    def test_add_new_book_add_two_books_count_books_two(self, books_collector):
        books_collector.add_new_book(book1)
        books_collector.add_new_book(book2)
        assert len(books_collector.get_books_rating()) == 2, 'Книги не добавляются'

    def test_add_new_book_add_two_same_books_count_books_one(self, books_collector):
        books_collector.add_new_book(book1)
        books_collector.add_new_book(book1)
        assert len(books_collector.get_books_rating()) == 1, 'Добавлены те же книги'

    def test_set_book_rating_add_rating_to_nonexistent_book_rating_is_none(self, books_collector):
        books_collector.set_book_rating(book1, 10)
        assert books_collector.get_book_rating(book1) is None, 'Установлен рейтинг несуществующей книги'

    @pytest.mark.parametrize('rating', [-2, 20])
    def test_set_book_rating_add_new_book_with_out_of_range_one_to_ten_rating_rating_not_change(self, books_collector,
                                                                                                rating):
        books_collector.add_new_book(book1)
        books_collector.set_book_rating(book1, rating)
        assert books_collector.get_book_rating(book1) != rating, 'Рейтинг находится вне диапазона'

    def test_get_book_rating_get_nonexistent_book_rating_rating_is_none(self, books_collector):
        assert books_collector.get_book_rating(book1) is None, 'Рейтинг несуществующей книги равен получению'

    def test_add_book_in_favorites_add_new_book_book_in_favorites(self, books_collector):
        books_collector.add_new_book(book1)
        books_collector.add_book_in_favorites(book1)
        assert book1 in books_collector.get_list_of_favorites_books(), 'Книга не добавлена в избранное'

    def test_get_books_with_specific_rating_add_three_new_books_one_book_with_rating_more_than_eight(self,
                                                                                                     books_collector):
        for book, book_rating in books_with_ratings.items():
            books_collector.add_new_book(book)
            books_collector.set_book_rating(book, book_rating)
        assert len(books_collector.get_books_with_specific_rating(10)) == 1, 'Ни одной книги с рейтингом более десяти'

    def test_delete_book_from_favorites_add_new_book_to_favorites_count_of_books_is_zero(self, books_collector):
        books_collector.add_new_book(book1)
        books_collector.add_book_in_favorites(book1)
        books_collector.delete_book_from_favorites(book1)
        assert len(books_collector.get_list_of_favorites_books()) == 0, 'Книга не была удалена'
