from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Type(models.Model):
    """Тип документа"""
    title = models.CharField("Тип документа", max_length=150)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тип документа'
        verbose_name_plural = 'Тип документа'


class Documents(models.Model):
    """Приказы"""
    type = models.ForeignKey(
        Type,
        verbose_name="Тип документа",
        null=True,
        on_delete=models.SET_NULL,
        related_name="type_document"
    )
    title = models.CharField("Название", max_length=500)
    number = models.IntegerField("Номер", null=True)
    date_create = models.DateField(null=True)
    pub_date = models.DateField(auto_now_add=True)
    file = models.FileField(
        "Файл",
        upload_to="documents/%Y/%m/%d/"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='author_document',
        blank=True,
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
