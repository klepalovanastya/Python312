from django import forms
from django.core.exceptions import ValidationError
from my_app.models import Tasks

def check_not_empty(text):
    blocker_symbols = ['<', '>', '=']# список недопустимых символов
    for symbol in blocker_symbols:
        if symbol in text:
            raise ValidationError("Запрещенные символы")
    return text
class AddTaskForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}),

    )
    title = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 40, 'rows': 5}),

    )

    class Meta:
        model = Tasks
        fields = '__all__'
        labels = {'description': 'Описание','title':'Название', 'status':'Статус'}
    #Валидация описания задачи
    def clean_description(self):
        description = self.cleaned_data['description']
        if len(description) > 200:
            raise ValidationError("Максимальная длина описания - 200 символов")

        return description

    # Валидация статуса задачи
    def clean_status(self):
        status = self.cleaned_data['status']
        if status not in ["в процессе", "завершено"]:
            raise ValidationError("Недоспустимое название статуса")

        return status

    # Валидация названия задачи
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 100:
            raise ValidationError("Максимальная длина название - 100 символов")

        return title