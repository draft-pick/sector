from django.contrib.auth import get_user_model

from django.db import models

User = get_user_model()

ROLES_CHOICES = (
    ("ADMIN", "Администратор"),
    ("USER", "Пользователь"),
)


class RoleUsers(models.Model):
    """Пользовательские роли"""
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_role'
    )
    roles = models.CharField(max_length=9,
                             choices=ROLES_CHOICES, )

    def __str__(self):
        return f"{self.user} - {self.roles}"

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'




