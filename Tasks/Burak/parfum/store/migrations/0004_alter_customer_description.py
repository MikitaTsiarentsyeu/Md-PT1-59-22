# Generated by Django 4.1.5 on 2023-02-22 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_rename_amount_orderitem_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='description',
            field=models.TextField(),
        ),
    ]
