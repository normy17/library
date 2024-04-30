from django import forms
from django.core.exceptions import ValidationError

from web.models import *


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'publication_year', 'publisher', 'num_pages', 'num_copies')
        widgets = {
            'publication_year': forms.NumberInput(attrs={'min': '0'}),
            'num_pages': forms.NumberInput(attrs={'min': '1'}),
            'num_copies': forms.NumberInput(attrs={'min': '0'})
        }


class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ('full_name', 'phone')

    def clean_phone(self):
        value = self.cleaned_data.get('phone')
        if not value.replace(' ', '').replace('-', '').isdigit():
            raise ValidationError("Пожалуйста, используйте только цифры, пробелы и тире.")
        return value


class CardForm(forms.ModelForm):
    class Meta:
        model = VisitorCard
        fields = ('visitor', 'borrowed_date')
        widgets = {'borrowed_date': forms.DateInput(attrs={'type': 'date'})}
