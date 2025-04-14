import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    def test_add_book_in_favorites(self, collector):
        collector.add_new_book('Синяя')
        collector.add_book_in_favorites('Синяя')
        favorites = collector.get_list_of_favorites_books()
        assert 'Синяя' in favorites

    def test_add_book_in_favorites_len(self,collector):
        collector.add_new_book('Перспективная и асинхронная база знаний')
        collector.add_book_in_favorites('Перспективная и асинхронная база знаний')
        favorites = collector.get_list_of_favorites_books()
        assert len(favorites) > 1

    @pytest.mark.parametrize(
        'name, collector_count',
        [
            (['Гордость и предубеждение и зомби'], 1),
            (['Гордость и предубеждение и зомби','Что делать, если ваш кот хочет вас убить'], 2),
            ([], 0)
        ]
    )
    def test_add_book_in_favorites_quantity(self, collector, name, collector_count):
        for collector_name in name:
            collector.add_new_book(collector_name)
        for collector_name in name:
            collector.add_book_in_favorites(collector_name)
        favorites = collector.get_list_of_favorites_books()
        assert len(favorites) == collector_count

    def test_set_book_genre(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Роман')
        assert collector.get_book_genre('Гордость и предубеждение и зомби') == 'Роман'

    def test_get_book_genre(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Роман')
        genre = collector.get_book_genre('Гордость и предубеждение и зомби')
        assert genre == 'Роман'

    def test_get_books_with_specific_genre(self,collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Роман')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Приключение')
        books = collector.get_books_with_specific_genre('Роман')
        assert 'Гордость и предубеждение и зомби' in books
        assert len(books) == 1

    def test_get_books_genre(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Роман')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Приключение')
        books_genre = collector.get_books_genre()
        assert len(books_genre) == 2 and 'Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить' in books_genre

    def test_get_books_for_children(self, collector):
        collector.add_new_book('Синяя')
        collector.set_book_genre('Синяя', 'Фэнтези')
        collector.add_new_book('Ходячие мертвецы')
        collector.set_book_genre('Ходячие мертвецы', 'Ужасы')
        children_books = collector.get_books_for_children()
        assert 'Синяя' in children_books and len(children_books) == 1 and 'Ходячие мертвецы' not in children_books

    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book('Синяя')
        collector.add_book_in_favorites('Синяя')
        collector.delete_book_from_favorites('Синяя')
        favorites = collector.get_list_of_favorites_books()
        assert 'Синяя' not in favorites and len(favorites) == 0

        def test_get_list_of_favorites_books(self, collector):
            collector.add_new_book('Синяя')
            collector.add_book_in_favorites('Синяя')
            favorites = collector.get_list_of_favorites_books()
            assert 'Синяя' in favorites and len(favorites) == 1

        @pytest.mark.parametrize(
            'name, collector_count',
            [
                (['Синяя'], 0),
                (['Синяя', 'Что делать, если ваш кот хочет вас убить'], 0),
                ([], 0)
            ]
        )
        def test_delete_book_from_favorites(self, collector, name, collector_count):
            for collector_name in name:
                collector.add_new_book(collector_name)
                collector.add_book_in_favorites(collector_name)
            for collector_name in name:
                collector.delete_book_from_favorites(collector_name)
            favorites = collector.get_list_of_favorites_books()
            assert len(favorites) == collector_count
    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()