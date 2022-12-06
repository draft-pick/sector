from django.urls import path

from .views import (index,
                    create,
                    create_type,
                    detail,
                    detail_user,
                    doc_favorite,
                    doc_unfavorite,
                    SearchResultsView
                    )

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('create_type/', create_type, name='create_type'),
    path('detail/<int:doc_id>/', detail, name='detail'),
    path('detail_user/<int:user_id>', detail_user, name='detail_user'),
    path('<int:doc_id>/favorite/', doc_favorite, name='doc_favorite'),
    path('<int:doc_id>/unfavorite/', doc_unfavorite, name='doc_unfavorite'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
]
