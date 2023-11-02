import uuid

from django.db import models


class Role(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    creation_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)

    users = models.ManyToManyField('User', through='UserRole')

    def __str__(self):
        return f"{self.name}"

    class Meta:
        db_table = "content\".\"role"
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'


class User(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    creation_date = models.DateTimeField(auto_now_add=True)
    telegram_id = models.BigIntegerField(null=True, default=None, blank=True, editable=False)
    telegram_username = models.CharField(max_length=50, default=None, blank=True, null=True)
    telegram_first_name = models.CharField(max_length=50, default=None, blank=True, null=True)
    telegram_last_name = models.CharField(max_length=50, default=None, blank=True, null=True)
    telegram_full_name = models.CharField(max_length=50, default=None, blank=True, null=True)
    roles = models.ManyToManyField(Role, through='UserRole')

    def __str__(self):
        return f'{self.telegram_full_name}'

    class Meta:
        db_table = "content\".\"user"
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class UserRole(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    role = models.ForeignKey('Role', on_delete=models.CASCADE)

    class Meta:
        db_table = "content\".\"user_role"
