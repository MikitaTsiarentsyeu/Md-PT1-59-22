# Generated by Django 4.1.5 on 2023-02-10 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Media_models',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='Title')),
                ('media_video', models.FileField(blank=True, upload_to='video/%Y/%m/%d/', verbose_name='Media_video')),
                ('media_img', models.ImageField(blank=True, upload_to='img/%Y/%m/%d/', verbose_name='Media_img')),
                ('post', models.TextField(blank=True, verbose_name='Post')),
                ('data_time_create', models.DateTimeField(auto_now_add=True)),
                ('data_time_update', models.DateTimeField(auto_now=True)),
                ('type_file', models.CharField(blank=True, choices=[('img', 'img'), ('video', 'video'), ('none', 'none')], max_length=100, verbose_name='File_type')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Media content',
                'ordering': ['-data_time_update', 'title'],
            },
        ),
    ]
