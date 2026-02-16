from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from .managers import user_manager
from apps.tenants.models import tenant
import uuid


class user(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    email = models.EmailField(unique=True)
    full_name = models.CharField(max_length=255)

    tenant = models.ForeignKey(
        tenant,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    role = models.CharField(
        max_length=50,
        choices=[
            ("super_admin", "super_admin"),
            ("admin", "admin"),
            ("employee", "employee"),
        ]
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = "email"

    objects = user_manager()

    class Meta:
        db_table = "user"
