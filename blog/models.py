from django.db import models
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 100)
    body = models.TextField()
    discription = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add = True)
    modified_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='media/', null=True)

    def __str__(seft):
        return seft.title + ": " + seft.body
    