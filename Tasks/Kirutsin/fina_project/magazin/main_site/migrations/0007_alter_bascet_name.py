# Generated by Django 4.1.5 on 2023-02-24 20:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_site', '0006_bascet_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bascet',
            name='name',
            field=models.ForeignKey(blank=True, max_length=100, on_delete=django.db.models.deletion.CASCADE, to='main_site.products'),
        ),
    ]
