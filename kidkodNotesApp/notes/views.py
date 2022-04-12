from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from .forms import CreateNoteModelForm
from .models import NotesModel
from django.views.generic import ListView, CreateView, FormView

# Create your views here.
class NotesHomepageView(ListView, FormView):
    template_name = 'index.html'
    queryset = NotesModel.objects.all()

    def get(self, request, *args, **kwargs):
        form = CreateNoteModelForm()
        return render(request, self.template_name, {'form': form, 'notes': self.queryset})

    def post(self, request, *args, **kwargs):
        form = CreateNoteModelForm(request.POST)
        if form.is_valid():
            header = form.cleaned_data.get('header')
            body = form.cleaned_data.get('body')
            status = form.cleaned_data.get('status')
            new_note = NotesModel.objects.create(header=header, body=body, status=status)
            new_note.save()
        return redirect('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = self.queryset
        context['form'] = CreateNoteModelForm()
        return context

class CreateNoteView(CreateView):
    model = NotesModel
    form_class = CreateNoteModelForm
    template_name = 'index.html'
    success_url = reverse_lazy('index')

def change_status(request, pk):
    note = get_object_or_404(NotesModel, id=pk)
    if note.status == True:
        note.status = False
    else:
        note.status = True
    note.save()
    return redirect('index')