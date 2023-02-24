from django.contrib import admin
from .models import Author, Post, Oil, Contact, Category

admin.site.register(Author)
admin.site.register(Post)
admin.site.register(Oil)
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)
