from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    class TypeChoices(models.TextChoices):
        ADMIN = "ADM", _("Admin")
        TEACHER = "TEA", _("Teacher")
        STUDENT = "STU", _("Student")

    type = models.CharField(
                max_length=3,
                choices=TypeChoices,
                null=True,
                default=TypeChoices.STUDENT,
                )

    

