from django.db import models


# Create your models here
class Post(models.Model):
    POST_TYPES = [('c', 'copyright'), ('m', 'merket')]
    title = models.CharField(max_length=100)
    subtitle = models.CharField(blank = True, max_length=200)
    content = models.TextField()
    issued = models.DateTimeField()
    post_type = models.CharField(choices=POST_TYPES, max_length=1, blank=True)
    image = models.ImageField(upload_to='uploads', blank = True)#можно без картинки сохранить
    
    author= models.ForeignKey('Author', on_delete=models.CASCADE)#связь со сторой таблицей, каскад - если удаляется автор - удаляются посты
    
class Author (models.Model):
    email = models.EmailField(primary_key=True)#это первичный ключ
    name = models.CharField(max_length=100)
    
class DT(models.Model):
    name =  models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField()
    time = models.TimeField()