from main import BooksCollector
import pytest

class TestBooksCollector:

    @pytest.fixture
    def books_collector(self):
        return BooksCollector()

    @pytest.fixture
    def book1(self):
        return "Book 1"

    @pytest.fixture
    def book2(self):
        return "Book 2"

    def test_add_new_book_add_two_books(self, books_collector):
        # создаем экземпляр (объект) класса BooksCollector
        books_collector.add_book('Гордость и предубеждение и зомби')
        books_collector.add_book('Что делать, если ваш кот хочет вас убить')
        assert len(books_collector.get_books_rating()) == 2

    @pytest.mark.parametrize("rating, expected_result", [
        (5, ["Book 1"]),
        (3, ["Book 2"]),
        (1, [])
    ])
    def test_get_books_by_rating(self, books_collector, book1, book2, rating, expected_result):
        # Получение книги по рейтингу
        books_collector.add_book(book1)
        books_collector.add_book(book2)
        books_collector.set_book_rating(book1, 5)
        books_collector.set_book_rating(book2, 3)
        # Сравниваем списки слева и справа
        assert books_collector.get_books_by_rating(rating) == expected_result


    def test_add_same_book_to_favorites(self, books_collector, book1):
        # Добавим книгу
        books_collector.add_book(book1)
        # Пытаемся два раза добавить в фавориты
        books_collector.add_to_favorites(book1)
        books_collector.add_to_favorites(book1)
        # Проверяем, что длина избранных книг не изменилась
        assert len(books_collector.get_favorites()) == 1


    def test_add_book_with_empty_name(self, books_collector):
        # Добавление книги с пустым названием
        books_collector.add_book("")
        assert books_collector.get_books_rating() == {"": 1}

    def test_add_book_with_special_characters(self, books_collector):
        # Добавление книг со специальными символами
        book_name = "C++ Programming for Beginners [Special Edition]\n"
        books_collector.add_book(book_name)
        assert book_name in books_collector.get_books_rating()

    # Тут мы добавим параметризацию с двумя проверками двух книг
    # Таким образом, при каждом вызове теста для каждой книги из book будет вызываться фикстура
    # books_collector и создаваться объект BooksCollector()
    @pytest.mark.parametrize("book", [
        book1,
        book2
    ])
    def test_remove_book_that_does_not_exist(self, books_collector, book):
        # Удаление книги из избранных, которой нет.
        books_collector.add_book(book)
        books_collector.remove_from_favorites(book)
        books_collector.set_book_rating(book, 5)
        # Смотрим, что рейтинг книги, а значит и сама книга остались на месте
        assert books_collector.get_books_rating() == {book: 5}

    def test_add_book(self, books_collector, book1):
        # Проверяем добавление книги.
        books_collector.add_book(book1)

        # Проверяем, что книга есть в избранном
        assert book1 in books_collector.get_books_rating()

        # Проверяем, что повторное добавление книги не изменяет ее рейтинг.
        books_collector.add_book(book1)
        assert books_collector.get_books_rating()[book1] == 1

    def test_set_book_rating(self, books_collector, book1, book2):
        # Проверяем установку рейтинга книги.
        books_collector.add_book(book1)
        books_collector.set_book_rating(book1, 5)
        assert books_collector.get_book_rating(book1) == 5

        # Проверяем, что установка рейтинга не возможна для книги, которой нет в списке.
        books_collector.set_book_rating(book2, 5)
        assert books_collector.get_book_rating(book2) is None

        # Проверяем, что рейтинг не может быть меньше 1.
        books_collector.set_book_rating(book1, 0)
        assert books_collector.get_book_rating(book1) == 5

        # Проверяем, что рейтинг не может быть больше 10.
        books_collector.set_book_rating(book1, 11)
        assert books_collector.get_book_rating(book1) == 5

    def test_add_to_favorites(self, books_collector, book1, book2):
        # Проверяем добавление книги в избранное.
        books_collector.add_book(book1)
        books_collector.add_to_favorites(book1)
        assert book1 in books_collector.get_favorites()

        # Проверяем, что книгу нельзя добавить в избранное, если её нет в словаре books_rating.
        books_collector.add_to_favorites(book2)

        # Проверяем, нет ли левого объекта (книги) в спике избранных
        assert book2 not in books_collector.get_favorites()

    def test_remove_from_favorites(self, books_collector, book1):
        # Проверяем удаление книги из избранного.
        books_collector.add_book(book1)
        books_collector.add_to_favorites(book1)
        books_collector.remove_from_favorites(book1)

        # Проверяем, нет ли левого объекта (книги) в спике избранных
        assert book1 not in books_collector.get_favorites()

    @pytest.mark.parametrize("book_name, expected_result", [
        ("", {"": 1}),
        ("C++ Programming for Beginners [Special Edition]\n", {"C++ Programming for Beginners [Special Edition]\n": 1})
    ])
    def test_add_book_with_special_cases(self, books_collector, book_name, expected_result):
        # Добавление книг со специальными случаями: с пустым названием и с названием, содержащим специальные символы.
        books_collector.add_book(book_name)
        assert books_collector.get_books_rating() == expected_result

    def test_get_books_rating(self, books_collector, book1):
        # Получение рейтингов книг
        books_collector.add_book(book1)
        books_collector.set_book_rating(book1, 5)
        assert books_collector.get_books_rating() == {book1: 5}
