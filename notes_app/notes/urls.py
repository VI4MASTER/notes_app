from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create_note, name="create_note"),
    path("note/<int:note_id>/", views.note_detail, name="note_detail"),
]