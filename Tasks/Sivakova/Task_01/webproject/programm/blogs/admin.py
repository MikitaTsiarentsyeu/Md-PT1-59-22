from django.contrib import admin
from .models import Articles, Visitors, Comments, Doctors

admin.site.register(Articles)
admin.site.register(Visitors)
admin.site.register(Comments)
admin.site.register(Doctors)

# Register your models here.
