from django.db import models

# Create your models here.
class comments(models.Model):
    message = models.TextField(max_length=200)

    def __str__(self) :
        return f"{self.id}. {self.message[0:15]} ..."