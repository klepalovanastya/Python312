from django import forms
from my_app.models import Tasks


class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = '__all__'
        labels = {'description': 'Описание','title':'Название', 'status':'Статус'}
        widgets = {
            'description': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }