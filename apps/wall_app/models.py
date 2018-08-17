from django.db import models

# Create your models here.
class Message(models.Model):
    text = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class comments(models.Model):
    text = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)   
    messages = models.ForeignKey(Message,related_name="message_comment", on_delete=models.CASCADE)