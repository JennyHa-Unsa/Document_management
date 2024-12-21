from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('employee', 'Employee'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    # Ajusta los campos problemáticos con related_name
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups",  # Cambia el nombre relacionado
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",  # Cambia el nombre relacionado
        blank=True,
    )
