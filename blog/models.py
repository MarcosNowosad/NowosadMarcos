from django.db import models
import datetime
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/images', null=True, default="")
    image2 = models.ImageField(upload_to='blog/images/post',default="", blank=True)
    image3 = models.ImageField(upload_to='blog/images/post',default="", blank=True)
    image4 = models.ImageField(upload_to='blog/images/post',default="", blank=True)


    date = models.DateField(datetime.date.today)


    def __str__(self):
        return self.title
