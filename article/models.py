from django.db import models
from django.contrib.auth.models import User
from datetime import date

# Create your models here.
class Area (models.Model):
    name = models.CharField(max_length= 50, unique=True)
    description = models.CharField(max_length= 150)
    def __str__(self):
        return self.name


class Article (models.Model):
    title = models.CharField(max_length= 150)
    description = models.CharField(max_length= 200 )
    article = models.TextField(default ='')
    publication_date = models.DateField(default= date.today)
    viewable_admin = models.BooleanField(default= True)
    area = models.ForeignKey(Area, related_name = 'articles', on_delete = models.CASCADE)
    
    def __str__(self):
        return self.title
