import os
from uuid import uuid4

from django.contrib.auth import get_user_model
from django.db import models
import datetime as dt

# from validators import validate_file_extension, path_and_rename

User = get_user_model()

current = dt.datetime.now()


def path_and_rename(path):
    """Генератор имени файла сохранения."""

    def wrapper(instance, filename):
        ext = filename.split(".")[-1]
        filename = "{}.{}".format(uuid4().hex, ext)
        return os.path.join(path, filename)

    return wrapper


class Type(models.Model):
    """Тип документа"""
    title = models.CharField("Тип документа", max_length=150)
    color = models.CharField(
        max_length=7,
        verbose_name="Цвет в HEX",
    )

    class Meta:
        verbose_name = 'Тип документа'
        verbose_name_plural = 'Тип документа'
        constraints = [
            models.UniqueConstraint(
                fields=(
                    "title",
                    "color",
                ),
                name="unique_tag_name_color",
            )
        ]

    def __str__(self):
        return self.title


class Executor(models.Model):
    """Исполнители."""
    name = models.CharField("ФИО", max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Исполнитель'
        verbose_name_plural = 'Исполнители'


class Documents(models.Model):
    """Приказы"""
    type = models.ForeignKey(
        Type,
        verbose_name="Тип документа",
        null=True,
        on_delete=models.SET_NULL,
        related_name="type_document",
        blank=True,
    )
    title = models.CharField("Название", max_length=500)
    number = models.IntegerField("Номер", null=True)
    date_create = models.DateField(null=True)
    pub_date = models.DateField(auto_now_add=True)
    executor = models.ForeignKey(
        Executor,
        on_delete=models.CASCADE,
        related_name='executor_document',
        blank=True,
        null=True,
    )
    file = models.FileField(
        blank=False,
        upload_to=path_and_rename(f"documents/{current.year}/{current.month}"),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='author_document',
        null=True,
    )
    under_document = models.ForeignKey('self',
                                       on_delete=models.CASCADE,
                                       related_name='main_document',
                                       null=True,
                                       blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'


class Favorites(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorite_user',
    )
    document = models.ForeignKey(
        Documents,
        on_delete=models.CASCADE,
        related_name='favorite_doc',
    )

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранное'


class Comment(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comment_user',
    )
    document = models.ForeignKey(
        Documents,
        on_delete=models.CASCADE,
        related_name='comment_doc',
    )
    text = models.TextField(verbose_name='Текст')

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
