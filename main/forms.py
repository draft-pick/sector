from django import forms
from django.forms import ModelForm, TextInput, Textarea, FileInput, ImageField, Select

from .models import Documents, Type


class TypeForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Название'}))

    class Meta:
        model = Type
        fields = ('title',)


class DocumentForm(forms.ModelForm):
    type = forms.ModelChoiceField(queryset = Type.objects.all(),
                                  widget=forms.Select(attrs={'class':'select'}),
                                  empty_label='---Выберете тип---'
                                  )
    number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Номер'}))
    date_create = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Дата создания'}))

    class Meta:
        model = Documents
        fields = ('type', 'title', 'number', 'date_create', 'file',)

        widgets = {
            'type': Select(attrs={
                'class': 'select',
                'placeholder': 'Тип документа',
            }),
            'title': TextInput(attrs={
                'placeholder': 'Название'
            }),
            'file': FileInput(attrs={
                'class': 'file',
                'placeholder': 'Файлы',
            }),

        }

        # help_texts = {
        #     'text': 'Текст нового поста',
        #     'group': 'Группа, к которой будет относиться пост'
        # }
        # labels = {
        #     'text': 'Текст поля',
        #     'group': 'Группа'
        # }
