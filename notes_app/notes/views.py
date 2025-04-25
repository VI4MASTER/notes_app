from django.shortcuts import render
from datetime import datetime


def index(request):
    # Тестові дані для нотаток
    test_notes = [
        {
            'title': 'Нотатки з наради',
            'content': 'Обговорення графіку проєкту та розподілу ресурсів.',
            'created_at': datetime(2025, 4, 25, 10, 30)
        },
        {
            'title': 'Список покупок',
            'content': 'Молоко, яйця, хліб та фрукти.',
            'created_at': datetime(2025, 4, 24, 15, 45)
        },
        {
            'title': 'Ідея',
            'content': 'Створити нову функцію для автентифікації користувачів.',
            'created_at': datetime(2025, 4, 23, 9, 0)
        }
    ]

    return render(request, 'notes/index.html', {'notes': test_notes})