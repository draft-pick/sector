from django.contrib import admin

from .models import Type, Executor, Documents, Comment

admin.site.register(Type)

admin.site.register(Executor)

admin.site.register(Documents)

admin.site.register(Comment)
