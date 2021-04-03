from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default="My Freakin Awesome Blog!")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    post_date = models.DateTimeField(default=timezone.now, blank=True, null=True)


    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self): #This is to redirect page and in this Case we have to import "from django.urls import reverse"
        #return reverse('article-detail', args=(str(self.id)))
        return reverse('home')