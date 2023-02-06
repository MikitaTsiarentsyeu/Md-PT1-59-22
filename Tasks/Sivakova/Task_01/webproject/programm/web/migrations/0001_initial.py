# Generated by Django 4.1.5 on 2023-01-22 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('subtitle', models.CharField(blank=True, max_length=200)),
                ('content', models.TextField()),
                ('issued', models.DateTimeField()),
                ('image', models.ImageField(blank=True, upload_to='uploads')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.author')),
            ],
        ),
    ]
