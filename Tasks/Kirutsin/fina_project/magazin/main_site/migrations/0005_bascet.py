# Generated by Django 4.1.5 on 2023-02-24 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0004_alter_products_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bascet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('currency', models.CharField(choices=[('USD', 'USD'), ('RUB', 'RUB')], max_length=3)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
