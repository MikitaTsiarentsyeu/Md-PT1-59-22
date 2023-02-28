from django import forms
from .models import Post
from django.core.exceptions import ValidationError

class AddPost(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder":"Information about your image name and size"}))
    class Meta:
        model = Post
        fields = ('title', 'image')
