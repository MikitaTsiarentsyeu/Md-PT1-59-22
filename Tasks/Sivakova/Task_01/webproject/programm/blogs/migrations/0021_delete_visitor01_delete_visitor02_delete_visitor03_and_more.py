# Generated by Django 4.1.5 on 2023-02-01 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0020_visitor01_optionvartwo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Visitor01',
        ),
        migrations.DeleteModel(
            name='Visitor02',
        ),
        migrations.DeleteModel(
            name='Visitor03',
        ),
        migrations.DeleteModel(
            name='Visitor04',
        ),
        migrations.RenameField(
            model_name='visitors',
            old_name='optionvar',
            new_name='optionvarone',
        ),
        migrations.AddField(
            model_name='visitors',
            name='optionvarfive',
            field=models.CharField(choices=[('Первичный осмотр', 'Первичный осмотр'), ('Терапия', 'Терапия'), ('Стоматология', 'Стоматология'), ('Хирургия', 'Хирургия'), ('Кастрация/стерилизация', 'Кастрация/стерилизация')], default='Кастрация/стерилизация', max_length=100, verbose_name='Вид услуги'),
        ),
        migrations.AddField(
            model_name='visitors',
            name='optionvarfour',
            field=models.CharField(choices=[('Первичный осмотр', 'Первичный осмотр'), ('Терапия', 'Терапия'), ('Стоматология', 'Стоматология'), ('Хирургия', 'Хирургия'), ('Кастрация/стерилизация', 'Кастрация/стерилизация')], default='Хирургия', max_length=100, verbose_name='Вид услуги'),
        ),
        migrations.AddField(
            model_name='visitors',
            name='optionvarthree',
            field=models.CharField(choices=[('Первичный осмотр', 'Первичный осмотр'), ('Терапия', 'Терапия'), ('Стоматология', 'Стоматология'), ('Хирургия', 'Хирургия'), ('Кастрация/стерилизация', 'Кастрация/стерилизация')], default='Стоматология', max_length=100, verbose_name='Вид услуги'),
        ),
        migrations.AddField(
            model_name='visitors',
            name='optionvartwo',
            field=models.CharField(choices=[('Первичный осмотр', 'Первичный осмотр'), ('Терапия', 'Терапия'), ('Стоматология', 'Стоматология'), ('Хирургия', 'Хирургия'), ('Кастрация/стерилизация', 'Кастрация/стерилизация')], default='Терапия', max_length=100, verbose_name='Вид услуги'),
        ),
    ]
