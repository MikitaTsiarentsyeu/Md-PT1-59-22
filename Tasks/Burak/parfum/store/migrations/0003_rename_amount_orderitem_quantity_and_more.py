# Generated by Django 4.1.5 on 2023-02-22 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_customer_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='amount',
            new_name='quantity',
        ),
        migrations.AddField(
            model_name='order',
            name='transaction_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
