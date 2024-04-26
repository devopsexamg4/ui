from datetime import datetime,timedelta
from uuid import uuid4
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.validators import MaxValueValidator


def dockerdir(instance, _):
    """generate a path to save the uploaded dockerfile"""
    return f"assignments/{instance.user.id}/{str(uuid4())}/"

class User(AbstractUser):
    class TypeChoices(models.TextChoices):
        ADMIN = "ADM", _("Admin")
        TEACHER = "TEA", _("Teacher")
        STUDENT = "STU", _("Student")

    type = models.CharField(
        max_length = 3,
        choices = TypeChoices,
        null = True,
        default = TypeChoices.STUDENT,
        )

class Assignments(models.model):
    class StatusChoices(models.TextChoices):
        HIDDEN = "HID",_("Hidden")
        ACTIVE = "ACT",_("Active")
        PAUSED = "PAU",_("Paused")
        FINISHED = "FIN",_("Finished")
    
    status = models.CharField(
        max_length = 3,
        choices = StatusChoices,
        default = StatusChoices.HIDDEN
    )

    maxmemory = models.PositiveIntegerField(
        default = 100,
        validators = [ MaxValueValidator(1000) ]
    )

    maxcpu = models.PositiveIntegerField(
        default = 1,
        validators = [ MaxValueValidator(4) ]
    )

    timer = models.DurationField(
        default = timedelta(seconds = 120),
        validators = [ MaxValueValidator(timedelta(minutes = 10)) ]
    )
    
    start = models.DateTimeField(
        default = datetime.now()
    )
    
    end = models.DateTimeField(
        default = datetime.now() + timedelta(days = 14)
    )
    
    dockerfile = models.FileField(
        upload_to = dockerdir
    )
    
    maxsubs = models.PositiveIntegerField(
        default = 5,
        validators = [ MaxValueValidator(15) ]
    )


# class StudentSubmissions(models.model):
