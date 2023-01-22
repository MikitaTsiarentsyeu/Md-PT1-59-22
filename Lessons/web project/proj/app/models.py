from django.db import models

class Post(models.Model):

    POST_TYPES = [('c', "copyright material"), ('m', "marketing material")]

    title = models.CharField(max_length=100)
    subtitle = models.CharField(blank=True, max_length=300)
    content = models.TextField()
    issued = models.DateTimeField()
    post_type = models.CharField(choices=POST_TYPES, max_length=1)
    image = models.ImageField(upload_to='uploads', blank=True)

    author = models.ForeignKey('Author', on_delete=models.CASCADE)

class Author(models.Model):

    email = models.EmailField(primary_key=True)
    name = models.CharField(max_length=100)