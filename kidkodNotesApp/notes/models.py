from django.db import models

# Create your models here.
class NotesModel(models.Model):
    header = models.CharField(max_length=25, null=False, blank=False)
    body = models.CharField(max_length=200, null=False, blank=False)
    status = models.BooleanField(default=False)