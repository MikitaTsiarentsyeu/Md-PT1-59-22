from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='uploads', blank=True)
    author = models.ForeignKey('Author', on_delete=models.DO_NOTHING)
    issued = models.DateTimeField()
class Author(models.Model):

    email = models.EmailField(primary_key=True)
    name = models.CharField(max_length=100)