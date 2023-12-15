from .models import Add_Numbers
from django.forms import ModelForm, TextInput, Select


class CreateForm(ModelForm):
    class Meta:
        model = Add_Numbers
        fields = ['category_types', 'category_unaa', 'category_number', 'title', 'number']
        widgets = {
            "category_types": Select(attrs={
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
                'placeholder': 'Введите гос номер',

            }),
            "number": TextInput(attrs={
                "class": "form-control",
                'placeholder': 'Введите номер док:',

            }),
        }