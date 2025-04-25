from django.shortcuts import render, get_object_or_404, redirect
from .models import Note, Category
from .forms import NoteForm
from django.db.models import Q
from django.utils import timezone

def index(request):
    category_filter = request.GET.get('category', '')
    reminder_filter = request.GET.get('reminder', '')
    search_query = request.GET.get('search', '')

    notes = Note.objects.all().order_by('-created_at')

    # Фільтрування за категорією
    if category_filter:
        if category_filter == 'none':
            notes = notes.filter(category__isnull=True)
        else:
            notes = notes.filter(category__id=category_filter)

    # Фільтрування за нагадуванням
    if reminder_filter:
        now = timezone.now()
        if reminder_filter == 'today':
            notes = notes.filter(reminder__date=now.date())
        elif reminder_filter == 'future':
            notes = notes.filter(reminder__gt=now)
        elif reminder_filter == 'no_reminder':
            notes = notes.filter(reminder__isnull=True)

    # Пошук за заголовком
    if search_query:
        notes = notes.filter(title__icontains=search_query)

    categories = Category.objects.all()
    return render(request, 'notes/index.html', {
        'notes': notes,
        'categories': categories,
        'category_filter': category_filter,
        'reminder_filter': reminder_filter,
        'search_query': search_query,
    })

def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = NoteForm()
    return render(request, 'notes/create_note.html', {'form': form})

def note_detail(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == 'POST':
        if 'delete' in request.POST:
            note.delete()
            return redirect('index')
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = NoteForm(instance=note)
    return render(request, 'notes/note_detail.html', {'note': note, 'form': form})