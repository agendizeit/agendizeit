from django.db import models

# Create your models here.


class AgendaItem(models.Model):
    topic = models.CharField(max_length=150)
    text = models.TextField()

class SharingItem(models.Model):
    topic = models.CharField(max_length=150)
    text = models.TextField()


