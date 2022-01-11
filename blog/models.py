from django.db import models
import datetime
# Create your models here.
class Blog_Post(models.Model):
    title = models.CharField(max_length = 100)
    subject = models.CharField(max_length = 200)
    post = models.CharField(max_length=2000)
    date = models.DateField(default=datetime.date.today)
    
    def __str__(self):
        return self.title