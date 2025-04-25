from django.core.management.base import BaseCommand
from notes.models import Category, Note
from datetime import datetime, timedelta
from django.utils import timezone

class Command(BaseCommand):
    help = 'Наповнює базу даних тестовими даними для категорій і нотаток'

    def handle(self, *args, **kwargs):
        # Очищення існуючих даних (опціонально)
        Note.objects.all().delete()
        Category.objects.all().delete()

        # Створення категорій
        categories = [
            Category(title="Робота"),
            Category(title="Особисте"),
            Category(title="Ідеї"),
        ]
        Category.objects.bulk_create(categories)
        self.stdout.write(self.style.SUCCESS('Категорії створено.'))

        # Отримання створених категорій
        work_cat = Category.objects.get(title="Робота")
        personal_cat = Category.objects.get(title="Особисте")
        ideas_cat = Category.objects.get(title="Ідеї")

        # Створення нотаток
        notes = [
            Note(
                title="Нотатки з наради",
                text="Обговорення графіку проєкту та розподілу ресурсів.",
                reminder=timezone.make_aware(datetime(2025, 4, 26, 10, 0)),
                category=work_cat
            ),
            Note(
                title="Список покупок",
                text="Молоко, яйця, хліб та фрукти.",
                reminder=None,
                category=personal_cat
            ),
            Note(
                title="Ідея для проєкту",
                text="Створити нову функцію для автентифікації користувачів.",
                reminder=timezone.make_aware(datetime(2025, 4, 25, 9, 0)),
                category=ideas_cat
            ),
            Note(
                title="Без категорії",
                text="Тестова нотатка без категорії.",
                reminder=None,
                category=None
            ),
        ]
        Note.objects.bulk_create(notes)
        self.stdout.write(self.style.SUCCESS('Нотатки створено.'))