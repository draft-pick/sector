from django.urls import path

from .views import (index,
                    create,
                    create_type,
                    detail
                    )

app_name = 'main'

urlpatterns = [
    path('', index, name='index'),
    path('create/', create, name='create'),
    path('create_type/', create_type, name='create_type'),
    path('detail/<int:doc_id>/', detail, name='detail')
]
