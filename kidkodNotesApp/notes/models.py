from email.policy import default
from django.db import models
from django.utils import timezone

# Create your models here.
class NotesModel(models.Model):
    header = models.CharField(max_length=25, null=False, blank=False)
    body = models.TextField(max_length=200, null=False, blank=False)
    status = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-date']