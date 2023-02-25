from django import forms
from .models import Recipe, Ingredient, Rating, ProhibitedFoodstuff
from django.core.exceptions import ValidationError


class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = [
        'recipe_name',
        'recipe_type',
        'calories',
        'time',
        'preparation',
        'image']
        widgets = {
            'recipe_name': forms.TextInput(attrs={'type':'text2', 'label':'Recipe Name'}),
            'calories': forms.TextInput(attrs={'type':'text2'}),
            'time': forms.TextInput(attrs={'type':'text2'}),
            'preparation': forms.Textarea()
        }

    def clean_recipe_name(self):
        recipe_name = self.cleaned_data['recipe_name']
        if len(recipe_name) > 50:
            raise ValidationError('Recipe name exceeds the allowed limit of 50 characters')
        
        return recipe_name
    

    def clean_preparation(self):
        preparation = self.cleaned_data['preparation']
        if len(preparation) > 500:
            raise ValidationError('Preparation field exceeds the allowed limit of 500 characters')
        
        return preparation


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = [
        'name',
        'amount'
   ]
        widgets = {
            'name': forms.TextInput(attrs={'type':'text2'}),
            'amount': forms.TextInput(attrs={'type':'text2'})
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) > 50:
            raise ValidationError('Ingredient name exceeds the allowed limit of 50 characters')
        
        return name
    
    def clean_amount(self):
        amount = self.cleaned_data['amount']
        if len(amount) > 30:
            raise ValidationError('Ingredient amount field exceeds the allowed limit of 30 characters')
        
        return amount


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = [
        'value',
        'comment',
        'issued'
   ]

    def clean_comment(self):
        comment = self.cleaned_data['comment']
        if len(comment) > 500:
            raise ValidationError('Comment exceeds the allowed limit of 500 characters')
        
        return comment


class ProhibitedFoodstuffForm(forms.ModelForm):
    class Meta:
        model = ProhibitedFoodstuff
        fields = [
        'name',
        'reason'
   ]
        
    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) > 80:
            raise ValidationError('Prohibited Foodstuff name exceeds the allowed limit of 80 characters')
        
        return name
    
    def clean_reason(self):
        reason = self.cleaned_data['reason']
        if len(reason) > 80:
            raise ValidationError('Reason field exceeds the allowed limit of 80 characters')
        
        return reason