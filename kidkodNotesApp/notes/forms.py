from django import forms
from .models import NotesModel
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Button, Submit, Layout, Field, ButtonHolder

class CreateNoteModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-inline'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('header', css_class="form-control mb-2", PlaceHolder="Заголовок..."),
            Field('body', css_class="form-control mb-2", PlaceHolder="Описание..."),
            Field('status', css_class="form-check-input mb-2 text-info"),
            ButtonHolder (
                Submit('create', 'Добавить', css_class='btn btn-success mb-2')
            )
        )
    class Meta:
        model = NotesModel
        fields = [
            'header',
            'body',
            'status',
        ]
        labels = {
            'header': 'Заголовок',
            'body': 'Описание',
            'status': 'Статус',
        }

class EditNoteModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-inline'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Field('header', css_class="form-control mb-2", PlaceHolder="Заголовок..."),
            Field('body', css_class="form-control mb-2", PlaceHolder="Описание..."),
            Field('status', css_class="form-check-input mb-2 text-info"),
            ButtonHolder (
                Submit('edit', 'Изменить', css_class='btn btn-warning mb-2 fw-normal')
            )
        )
    class Meta:
        model = NotesModel
        fields = [
            'header',
            'body',
            'status'
        ]
        labels = {
            'header': 'Заголовок',
            'body': 'Описание',
            'status': 'Статус',
        }
