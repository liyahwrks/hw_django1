from django.core.management.base import BaseCommand
from store.models import Product, Category
from faker import Faker
import random


class Command(BaseCommand):
    help = 'Генерация тестовых данных для магазина'
    
    def handle(self, *args, **kwargs):
        fake = Faker()
        
        self.stdout.write('Начинаем генерацию данных')
        
        categories = []
        category_names = ['Студийные альбомы', 'Мини-альбомы', 'Синглы', 'Мерч']
        
        for name in category_names:
            category = Category.objects.create(
                name=name,
                description=fake.text(max_nb_chars=100)
            )
            categories.append(category)
        
        self.stdout.write('Завершили создание категорий')
        
        blackpink_albums = [
            'THE ALBUM', 'BORN PINK', 'SQUARE UP', 'KILL THIS LOVE',
            'BLACKPINK', 'AS IF ITS YOUR LAST', 'WHISTLE', 'BOOMBAYAH',
            'LOVESICK GIRLS', 'HOW YOU LIKE THAT', 'DDU-DU DDU-DU'
        ]
        
        for i in range(10):
            product = Product.objects.create(
                name=random.choice(blackpink_albums) + ' ' + fake.word(),
                category=random.choice(categories),
                price=random.randint(1000, 50000),
                description=fake.text(max_nb_chars=200)
            )
        
        self.stdout.write('Завершили создание товаров')
        self.stdout.write('Завершили генерацию данных')