from django import forms
from webapp.models import Task


class CustomDateInput(forms.DateInput):
    input_type = 'date'


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = '__all__'
        widgets = {
            'pub_date': CustomDateInput()
        }

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['text_for_detailed'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['class'] = 'form-control'
        self.fields['pub_date'].widget.attrs['class'] = 'form-control'
