from django import forms

from .models import Documents, Type


class TypeForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Название'}))

    class Meta:
        model = Type
        fields = ('title',)


class DocumentForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Название'}))

    class Meta:
        model = Documents
        fields = ('type', 'title', 'number', 'date_create', 'file', 'author',)

        # help_texts = {
        #     'text': 'Текст нового поста',
        #     'group': 'Группа, к которой будет относиться пост'
        # }
        # labels = {
        #     'text': 'Текст поля',
        #     'group': 'Группа'
        # }
