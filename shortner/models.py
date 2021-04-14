from django.db import models

# # Create your models here.
class shortner(models.Model):
    urls= models.CharField(max_length=10000)
    uuid=models.CharField(max_length=10)
    
    def __str__(self):
        return self.urls