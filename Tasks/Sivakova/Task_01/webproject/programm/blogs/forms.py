from .models import Articles, Visitors, Comments
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, IntegerField, ImageField
from django.core.exceptions import ValidationError



class ArticlesForm(ModelForm):
    class Meta:
        model  = Articles
        fields = ['titl', 'shorttitle', 'content', 'issued', 'image']
        widgets = {
            "title": TextInput(attrs = {'placeholder':'Название статьи'}),
            "shorttitle": TextInput(attrs = {'placeholder':'Главное о главном'}),
            "content": Textarea(attrs = {'placeholder':'Основная информация'}),
            "issued": DateTimeInput(attrs = {'placeholder':'Дата публикации'})
           
            
        }
        
class VisitorsForm(ModelForm):
    class Meta:
        model = Visitors
        fields = ['title', 'surname', 'option', 'optionvarone','content', 'email', 'date', 'month', 'time']
        widgets = {
            "title": TextInput(attrs = {'placeholder':'Фамилия', 'class': 'form-control'}),
            "surname": TextInput(attrs = {'placeholder':'Имя', 'class': 'form-control'}),
           
            "content": Textarea(attrs = {'placeholder':'Комментарии/пожелания', 'class': 'form-control'}),
            "email": TextInput(attrs = {'placeholder':'Ваш email', 'class': 'form-control'}),
           
           
        }
    def clean_title(self):
        print(self.cleaned_data)
    
        title = self.cleaned_data['title']
        email = self.cleaned_data['email']
        print(self.cleaned_data)
        if title == email:
         raise ValidationError('error means')
        return email
        
       
        
class VisitorsForm01(ModelForm):
    class Meta:
        model = Visitors
        fields = ['title', 'surname', 'option', 'optionvartwo','content', 'email', 'date','month', 'time']
        widgets = {
            "title": TextInput(attrs = {'placeholder':'Фамилия', 'class': 'form-control'}),
            "surname": TextInput(attrs = {'placeholder':'Имя', 'class': 'form-control'}),
            "email": TextInput(attrs = {'placeholder':'Ваш email', 'class': 'form-control'}),
           
            "content": Textarea(attrs = {'placeholder':'Комментарии/пожелания', 'class': 'form-control'}),
            
           
           
           
        }
    def clean_title(self):
        title = self.cleaned_data['title']
        email = self.cleaned_data['email']
        print(title, email)
        if title == email:
         raise ValidationError('error means')
        return email
        
class VisitorsForm02(ModelForm):
    class Meta:
        model = Visitors
        fields = ['title', 'surname', 'option', 'optionvarthree','content', 'email', 'date','month', 'time']
        widgets = {
            "title": TextInput(attrs = {'placeholder':'Фамилия', 'class': 'form-control'}),
            "surname": TextInput(attrs = {'placeholder':'Имя', 'class': 'form-control'}),
            "email": TextInput(attrs = {'placeholder':'Ваш email', 'class': 'form-control'}),
           
           
            "content": Textarea(attrs = {'placeholder':'Комментарии/пожелания', 'class': 'form-control'}),
             
       
        
            
        }
    def clean_title(self):
        title = self.cleaned_data['title']
        email = self.cleaned_data['email']
        print(title, email)
        if title == email:
         raise ValidationError('error means')
        return email
        
class VisitorsForm03(ModelForm):
    class Meta:
        model = Visitors
        fields = ['title', 'surname', 'option', 'optionvarfour','content', 'email', 'date','month', 'time']
        widgets = {
            "title": TextInput(attrs = {'placeholder':'Фамилия', 'class': 'form-control'}),
            "surname": TextInput(attrs = {'placeholder':'Имя', 'class': 'form-control'}),
           
            "email": TextInput(attrs = {'placeholder':'Ваш email', 'class': 'form-control'}),
            "content": Textarea(attrs = {'placeholder':'Комментарии/пожелания', 'class': 'form-control'}),
            
           
          
            
        }
    def clean_title(self):
        title = self.cleaned_data['title']
        email = self.cleaned_data['email']
        print(title, email)
        if title == email:
         raise ValidationError('error means')
        return email
    
class VisitorsForm04(ModelForm):
    class Meta:
        model = Visitors
        fields = ['title', 'surname', 'option', 'optionvarfive','content', 'email', 'date','month', 'time']
        widgets = {
            "title": TextInput(attrs = {'placeholder':'Фамилия', 'class': 'form-control'}),
            "surname": TextInput(attrs = {'placeholder':'Имя', 'class': 'form-control'}),
            "email": TextInput(attrs = {'placeholder':'Ваш email', 'class': 'form-control'}),
           
           
            "content": Textarea(attrs = {'placeholder':'Комментарии/пожелания', 'class': 'form-control'}),
            
        
            
        }
    def clean_title(self):
        title = self.cleaned_data['title']
        email = self.cleaned_data['email']
        print(title, email)
        if title == email:
         raise ValidationError('error means')
        return email
    
class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['name', 'surname', 'content', 'choice']
        widgets = {
            "name": TextInput(attrs = {'placeholder':'Имя', 'class': 'form-control'}),
            "surname": TextInput(attrs = {'placeholder':'Фамилия', 'class': 'form-control'}),
           
           
            "content": Textarea(attrs = {'placeholder':'Ваш отзыв', 'class': 'form-control'})
            
        
            
        }