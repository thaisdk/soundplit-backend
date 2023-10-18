from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from base.managers import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(max_length=200)
    created_date = models.DateField(auto_now_add=True)
    assembly_ai_api_key = models.CharField(max_length=256)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["name", "assembly_ai_api_key"]

    objects = UserManager()


class Recording(models.Model):
    created_date = models.DateField(auto_now_add=True)
    file = models.FileField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    recording_name = models.CharField(max_length=120)
    transcription_text = models.TextField(blank=True)
    transcription_progress = models.FloatField(default=0)
    transcription_time = models.IntegerField()

