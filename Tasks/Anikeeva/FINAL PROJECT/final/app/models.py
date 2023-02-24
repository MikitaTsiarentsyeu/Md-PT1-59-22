from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=150, db_index=True, verbose_name='Name category')
    slug = models.SlugField(max_length=150, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse('final:product_list_by_category', args=[self.slug])

class Oil(models.Model):

    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name='Choose category')
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=200, db_index=True)
    short_description = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='uploads', blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, verbose_name='Price')

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
            return reverse('final:product_detail', args=[self.id, self.slug])

class Post(models.Model):

    POST_TYPES = [('n', "news"), ('d', "discount")]

    title = models.CharField(max_length=300)
    subtitle = models.CharField(blank=True, max_length=300)
    content = models.TextField()
    issued = models.DateTimeField()
    post_type = models.CharField(choices=POST_TYPES, max_length=1)
    image = models.ImageField(upload_to='uploads', blank=True)

    author = models.ForeignKey('Author', on_delete=models.DO_NOTHING)

class Author(models.Model):

    email = models.EmailField(primary_key=True)
    name = models.CharField(max_length=100)

class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.email    