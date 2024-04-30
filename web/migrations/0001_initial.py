# Generated by Django 5.0.4 on 2024-04-30 15:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('author', models.CharField(max_length=50, verbose_name='Автор')),
                ('publication_year', models.IntegerField(verbose_name='Год издательства')),
                ('publisher', models.CharField(max_length=50, verbose_name='Издательство')),
                ('num_pages', models.IntegerField(verbose_name='Кол-во страниц')),
                ('num_copies', models.IntegerField(verbose_name='Количество экземпляров в библиотеке')),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='ФИО')),
                ('phone', models.CharField(max_length=15, verbose_name='Телефон')),
            ],
        ),
        migrations.CreateModel(
            name='VisitorCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrowed_date', models.DateField(verbose_name='Дата выдачи')),
                ('returned_date', models.DateField(blank=True, null=True, verbose_name='Дата возврата')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.book', verbose_name='Книга')),
                ('visitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.visitor', verbose_name='Посетитель')),
            ],
        ),
    ]
