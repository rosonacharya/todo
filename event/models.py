from django.db import models

# Create your models here
class task(models.Model):
    user = models.CharField(max_length=10)
    email = models.CharField(max_length=30)
    phone = models.CharField(max_length=10)
    list = models.TextField()
    
    def __str__(self):
        return self.user
    

    
