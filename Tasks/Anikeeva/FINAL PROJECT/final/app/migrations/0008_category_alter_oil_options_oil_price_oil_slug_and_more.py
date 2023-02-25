# Generated by Django 4.1.6 on 2023-02-23 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=150, verbose_name='Name category')),
                ('slug', models.SlugField(max_length=150, unique=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ('name',),
            },
        ),
        migrations.AlterModelOptions(
            name='oil',
            options={'ordering': ('name',), 'verbose_name': 'Product', 'verbose_name_plural': 'Products'},
        ),
        migrations.AddField(
            model_name='oil',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=15, verbose_name='Price'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='oil',
            name='slug',
            field=models.SlugField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterIndexTogether(
            name='oil',
            index_together={('id', 'slug')},
        ),
        migrations.RemoveField(
            model_name='oil',
            name='kind',
        ),
        migrations.AddField(
            model_name='oil',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='app.category', verbose_name='Choose category'),
            preserve_default=False,
        ),
    ]