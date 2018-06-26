from django.db import models

# Do I need this? 
import hashlib

#Can I make adding agenda items Admin only?
class AgendaItem(models.Model):
    topic = models.CharField(max_length=150)
    text = models.TextField() #This text should either go away or it should be for the admin to provide background information on the agenda item.

#Then I want a separate text box for different users to comments on the same agenda topic without adding another topic heading.
class Discuss (models.Model): 
    username = models.CharField(max_length=30)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)  
    image = models.FileField(upload_to='discuss_images/', null=True, blank=True) 

class SharingItem(models.Model):
    topic = models.CharField(max_length=150)
    text = models.TextField()    
    image = models.FileField(upload_to='share_images/', null=True, blank=True)    

