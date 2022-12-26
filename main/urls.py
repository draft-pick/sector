from django.urls import path

from .views import (
    index,
    create,
    create_type,
    detail,
    detail_user,
    doc_favorite,
    doc_unfavorite,
    SearchResultsView,
    documents_list,
    create_executor,
    create_include,
    detail_executor,
    edit_document,
)

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('create_type/', create_type, name='create_type'),
    path('create_executor/', create_executor, name='create_executor'),
    path('<int:doc_id>/create_include', create_include, name='create_include'),
    path('detail/<int:doc_id>/', detail, name='detail'),
    path('documents_list/', documents_list, name='documents_list'),
    path('detail/<int:doc_id>/edit', edit_document, name='edit_document'),
    path('detail_user/<int:user_id>', detail_user, name='detail_user'),
    path('executor/<int:executor_id>', detail_executor, name='detail_executor'),
    path('<int:doc_id>/favorite/', doc_favorite, name='doc_favorite'),
    path('<int:doc_id>/unfavorite/', doc_unfavorite, name='doc_unfavorite'),
    path('search/', SearchResultsView.as_view(), name='search_results'),

]
