from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.views.generic import ListView

from .models import Type, Documents
from .forms import TypeForm, DocumentForm


@login_required()
def index(request):
    """Главная страница."""
    documents = Documents.objects.all()
    types = Type.objects.annotate(sum_documents=Count('type_document'))

    def count_documents():
        sum_count = []

        for type in types:
            if type.sum_documents > 0:
                sum_count.append(type.sum_documents)
        return sum_count

    context = {
        'title': 'Главная страница',
        'documents': documents,
        'types': types,
        'type_count': count_documents()
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
    document = get_object_or_404(Documents, pk=doc_id)
    context = {
        'title': document.title,
        'document': document
    }
    return render(request, 'main/detail.html', context)


@login_required()
class SearchResultsView(ListView):
    model = Documents
    template_name = 'main/search_results.html'

    def get_queryset(self):  # новый
        return Documents.objects.filter(
            Q(name__icontains='Boston') | Q(state__icontains='NY')
        )
