from django.db import models
import datetime #used for date
# Create your models here.

class Blog(models.Model): #Created class for model
    title = models.CharField(max_length = 150) #used for title
    description = models.TextField()
    date = models.DateField(default=datetime.date.today) #Used to keep track of date
    
    def __str__(self): #returns the title
        return self.title