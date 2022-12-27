from django import forms
from django.forms import (
    TextInput,
    FileInput,
    NumberInput,
)

from .models import Documents, Type, Executor


class TypeForm(forms.ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Название'})
    )

    class Meta:
        model = Type
        fields = ('title',)


class DocumentForm(forms.ModelForm):
    type = forms.ModelChoiceField(
        queryset=Type.objects.all(),
        widget=forms.Select(attrs={'class': 'select'}),
        empty_label='---Выберете категорию---'
    )
    number = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Номер'})
    )
    date_create = forms.DateField(
        widget=NumberInput(attrs={'type': 'date'})
    )
    executor = forms.ModelChoiceField(
        queryset=Executor.objects.all(),
        widget=forms.Select(attrs={'class': 'select'}),
        empty_label='---Выберете исполнителя---',
        required=False
    )

    class Meta:
        model = Documents
        fields = ('type', 'title', 'number', 'date_create', 'executor', 'file')

        widgets = {
            'title': TextInput(attrs={
                'placeholder': 'Название'
            }),
            'file': FileInput(attrs={
                'class': 'file',
                'placeholder': 'Добавить файл',
            }),

        }


class ExecutorForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'ФИО'})
    )

    class Meta:
        model = Executor
        fields = ('name',)
