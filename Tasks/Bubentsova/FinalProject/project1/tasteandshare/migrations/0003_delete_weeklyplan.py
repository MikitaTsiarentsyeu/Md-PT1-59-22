# Generated by Django 4.1.5 on 2023-02-24 22:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasteandshare', '0002_alter_recipe_recipe_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='WeeklyPlan',
        ),
    ]
