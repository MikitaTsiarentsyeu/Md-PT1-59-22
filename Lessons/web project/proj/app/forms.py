from django import forms
from .models import Post
from django.core.exceptions import ValidationError

class AddPost(forms.Form):

    title = forms.CharField(max_length=100)
    subtitle = forms.CharField(max_length=300)
    content = forms.CharField(widget=forms.Textarea())
    post_type = forms.ChoiceField(choices=Post.POST_TYPES, label='post type')
    image = forms.ImageField()

    def clean_subtitle(self):
        title_data = self.cleaned_data['title']
        subtitle_data = self.cleaned_data['subtitle']

        if subtitle_data == title_data:
            raise ValidationError("The title and the subtitle should be different")

        return subtitle_data        


class AddPostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'subtitle', 'content', 'post_type', 'image')

    def clean_subtitle(self):
        title_data = self.cleaned_data['title']
        subtitle_data = self.cleaned_data['subtitle']

        if subtitle_data == title_data:
            raise ValidationError("The title and the subtitle should be different")

        return subtitle_data      