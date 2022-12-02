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
    # path('detail/<int:decree_id>/', decree_detail, name='decree_detail'),
    # path('detail/<int:decree_id>/create_changed/',
    #      decree_changed_create,
    #      name='decree_changed_create'),
    # path('detail/<int:decree_id>/detail_changed/<int:decree_changed_id>',
    #      decree_changed_detail,
    #      name='decree_changed_detail')
]
