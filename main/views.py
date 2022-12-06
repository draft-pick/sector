from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Count, Q
from django.views.generic import ListView
from django.contrib.auth import get_user_model

from .models import Type, Documents, Favorites
from users.models import RoleUsers
from .forms import TypeForm, DocumentForm

User = get_user_model()


@login_required()
def index(request):
    """Главная страница."""
    documents = Documents.objects.all()
    favorites = Favorites.objects.filter(user__username=request.user).values_list('document_id', flat=True)
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
        'favorites': favorites,
        'types': types,
        'type_count': count_documents()
    }
    return render(request, 'main/index.html', context)


@login_required()
def documents_list(request):
    """Список всех документов с фильтрами."""
    sort = request.GET.getlist('sort')
    documents = Documents.objects.all().order_by(*sort)

    context = {
        'title': 'Список всех документов',
        'documents': documents,
    }

    return render(request, 'main/documents_list.html', context)

@login_required()
def create_type(request):
    """Добавить новый тип документа."""
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
@permission_required('main.add_documents', raise_exception=True)
def create(request):
    """Добавить новый документ."""
    if not request.user.has_perm('main.add_documents'):
        raise PermissionDenied
    form = DocumentForm(request.POST or None)
    if form.is_valid():
        document = form.save(commit=False)
        document.author = request.user
        document.save()
        return redirect('main:index')
    context = {
        'title': 'Добавить новый документ',
        'form': form,
    }
    return render(request, 'main/create.html', context)


@login_required()
def detail(request, doc_id):
    """Детальный просмотр документа"""
    document = get_object_or_404(Documents, pk=doc_id)
    context = {
        'title': document.title,
        'document': document
    }
    return render(request, 'main/detail.html', context)


@login_required()
def detail_user(request, user_id):
    """Страница пользователя"""
    user = get_object_or_404(User, pk=user_id)
    favorites = Favorites.objects.filter(user__username=request.user).values_list('document_id', flat=True)
    context = {
        'title': f'Страница пользователя {user.first_name} {user.last_name}',
        'user': user,
        'favorites': favorites,
    }
    return render(request, 'main/detail_user.html', context)


class SearchResultsView(ListView):
    model = Documents
    template_name = 'main/search_results.html'
    extra_context = {'title': 'Поиск'}
    def get_queryset(self): # новый
        query = self.request.GET.get('q')
        object_list = Documents.objects.filter(
            Q(title__icontains=query) | Q(number__icontains=query)
        )
        return object_list


@login_required
def doc_favorite(request, doc_id):
    """Добавить документ в избранное."""
    document = get_object_or_404(Documents, pk=doc_id)
    Favorites.objects.get_or_create(user=request.user, document=document)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))


@login_required
def doc_unfavorite(request, doc_id):
    """Удалить документ из избранного."""
    document = get_object_or_404(Documents, pk=doc_id)
    Favorites.objects.filter(user=request.user, document=document).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))
