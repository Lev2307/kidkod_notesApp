"""notes_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from notes.views import NotesHomepageView, change_status, EditNoteView, DeleteNoteView, DeleteAllConfirmedNotesView, DeleteAllChosenNote, checkbox_delete_check

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', NotesHomepageView.as_view(), name="index"),
    path('change_status/<int:pk>/', change_status, name='change_status'),
    path('edit_note/<int:pk>/', EditNoteView.as_view(), name="edit_note"),
    path('delete_note/<int:pk>/', DeleteNoteView.as_view(), name="delete_note"),
    path('delete_all_confirmed_notes/', DeleteAllConfirmedNotesView.as_view(), name="delete_allconfirmed_note"),
    path('delete_selected/', DeleteAllChosenNote.as_view()),
    path('check/<int:pk>/', checkbox_delete_check),
]
