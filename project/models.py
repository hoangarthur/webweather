from django.db import models
# Create your models here.
class Proj(models.Model):
    title = models.CharField(max_length = 100)
    discription = models.CharField(max_length=100, null=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    modified_date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='media/', null=True)

    def __str__(seft):
        return seft.title + ": " + seft.body
    