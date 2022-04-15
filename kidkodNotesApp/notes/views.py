from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from .forms import CreateNoteModelForm, EditNoteModelForm
from .models import NotesModel
from django.views.generic.edit import FormMixin
from django.views.generic import ListView, UpdateView, DeleteView
from django.core.paginator import Paginator

# Create your views here.
class NotesHomepageView(ListView):
    template_name = 'index.html'
    model = NotesModel
    paginate_by = 4
    context_object_name = 'notes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CreateNoteModelForm()
        return context

    def post(self, request, *args, **kwargs):
        form = CreateNoteModelForm(request.POST)
        if form.is_valid():
            header = form.cleaned_data.get('header')
            body = form.cleaned_data.get('body')
            status = form.cleaned_data.get('status')
            new_note = NotesModel.objects.create(header=header, body=body, status=status)
            new_note.save()
        return redirect('index')

def change_status(request, pk):
    note = get_object_or_404(NotesModel, id=pk)
    if note.status == True:
        note.status = False
    else:
        note.status = True
    note.save()
    return redirect('index')

class EditNoteView(UpdateView):
    model = NotesModel
    form_class = EditNoteModelForm
    template_name = "edit_note.html"
    success_url = reverse_lazy('index')

class DeleteNoteView(DeleteView):
    model = NotesModel
    template_name = 'delete_note.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['note'] = get_object_or_404(NotesModel, pk=self.kwargs['pk'])
        context['pk'] = self.kwargs['pk']
        return context

class DeleteAllConfirmedNotesView(ListView):
    queryset = NotesModel.objects.filter(status=True)
    template_name = 'delete_all_confirmed_notes.html'
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        notes = NotesModel.objects.filter(status=True)
        return render(request, self.template_name, {'notes': notes})
    def post(self, request, *args, **kwargs):
        notes = NotesModel.objects.filter(status=True).delete()
        return redirect('index')