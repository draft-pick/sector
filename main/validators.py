import os
from uuid import uuid4

def path_and_rename(path):
    """Генератор имени файла сохранения."""
    def wrapper(instance, filename):
        ext = filename.split(".")[-1]
        filename = "{}.{}".format(uuid4().hex, ext)
        return os.path.join(path, filename)

    return wrapper
def validate_file_extension(value):
    """Проверка загружаемого формата файла."""
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')