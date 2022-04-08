from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import CreateNoteModelForm
from .models import NotesModel
from django.views.generic import ListView, CreateView

# Create your views here.
class NotesHomepageView(ListView):
    template_name = 'index.html'
    queryset = NotesModel.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = self.queryset
        context['form'] = CreateNoteModelForm()
        return context
    
    # def post(self, request, *args, **kwargs):
    #     return redirect('index')

class CreateNoteView(CreateView):
    model = NotesModel
    form_class = CreateNoteModelForm
    template_name = 'index.html'
    success_url = reverse_lazy('index')
