from django import forms
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget
from .models import Post
from django.core.exceptions import ValidationError


        
class AddPostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'subtitle', 'content', 'post_type', 'image')
    