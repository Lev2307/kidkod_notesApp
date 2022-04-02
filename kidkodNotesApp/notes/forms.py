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
            Field('header'),
            Field('body'),
            Field('status'),
            ButtonHolder (
                Submit('order', 'Order', css_class='btn btn-success')
            )
        )
    class Meta:
        model = NotesModel
        fields = [
            'header',
            'body',
            'status'
        ]
