import random
from faker import Faker


def generate_random_book():
    titles: ['Гордость и предубеждение и зомби', 'Что делать, если ваш кот хочет вас убить', 'Синяя', 'Перспективная и асинхронная база знаний', 'Ходячие мертвецы']
    return random.choice(titles)

fake = Faker('ru_RU')
def generate_random_book_title():
    return fake.catch_phrase()

print(generate_random_book_title())