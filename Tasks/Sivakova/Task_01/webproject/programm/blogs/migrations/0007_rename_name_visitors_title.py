# Generated by Django 4.1.5 on 2023-01-28 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0006_alter_articles_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visitors',
            old_name='name',
            new_name='title',
        ),
    ]
