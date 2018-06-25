from django.db import models

# Create your models here.


class AgendaItem(models.Model):
    topic = models.CharField(max_length=150)
    text = models.TextField()

class ItemDiscussion(models.Model):
    discussion = models.CharField(max_length=255)
    text = models.TextField()
