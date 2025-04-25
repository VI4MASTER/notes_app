from django.shortcuts import render
from .models import Note

def index(request):
    notes = Note.objects.all().order_by('-created_at')
    return render(request, 'notes/index.html', {'notes': notes})