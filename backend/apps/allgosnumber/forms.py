from .models import Add_Numbers
from django.forms import ModelForm, TextInput, Select


class CreateForm(ModelForm):
    class Meta:
        model = Add_Numbers
        fields = ['category_region', 'category_unaa', 'category_number', 'title']
        widgets = {
            "category_region": Select(attrs={
                "class": "form-select",
                'placeholder': 'Выберите регион',
            }),
            "category_unaa": Select(attrs={
                "class": "form-select",
                'placeholder': 'Выберите отдел',
            }),
            "category_number": Select(attrs={
                "class": "form-select",
                'placeholder': 'Выберите гос номер',
            }),
            "title": TextInput(attrs={
                "class": "form-control",
                'placeholder': 'Введите номер',

            }),
        }