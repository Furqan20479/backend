from django.db import models

# Create your models here.
class Index(models.Model):
    
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone =models.IntegerField()
    desc = models.CharField(max_length=120)

    def __str__(self):
        return self.name
    