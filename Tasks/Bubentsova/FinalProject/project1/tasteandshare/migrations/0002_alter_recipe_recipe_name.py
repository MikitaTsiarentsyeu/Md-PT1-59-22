# Generated by Django 4.1.5 on 2023-02-24 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasteandshare', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Recipe name'),
        ),
    ]
