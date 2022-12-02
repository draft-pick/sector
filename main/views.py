from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


from .models import Type, Documents
from .forms import TypeForm, DocumentForm


@login_required()
def index(request):
    """Главная страница."""
    documents = Documents.objects.all()
    context = {
        'title': 'Главная страница',
        'documents': documents,
    }
    return render(request, 'main/index.html', context)


@login_required()
def create(request):
    """Добавить новый документ."""
    form = DocumentForm(request.POST or None)
    if form.is_valid():
        document = form.save(commit=False)
        document.save()
        return redirect('main:index')
    context = {
        'title': 'Добавить новый документ',
        'form': form,
    }
    return render(request, 'main/create.html', context)


@login_required()
def create_type(request):
    types = Type.objects.all()
    type_form = TypeForm(request.POST or None)
    if type_form.is_valid():
        type_doc = type_form.save(commit=False)
        type_doc.save()
        return redirect('main:index')
    context = {
        'title': 'Добавить новый тип документа',
        'type_form': type_form,
        'types': types,
        'is_type': True,
    }
    return render(request, 'main/create.html', context)


@login_required()
def detail(request, doc_id):
    pass
    # document = get_object_or_404(Documents, pk=doc_id)
    # context = {
    #     'title': document.title,
    #     'document': document
    # }
    # render(request, 'main/detail.html', context)


