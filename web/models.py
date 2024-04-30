from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    author = models.CharField(max_length=50, verbose_name='Автор')
    publication_year = models.IntegerField(verbose_name='Год издательства')
    publisher = models.CharField(max_length=50, verbose_name='Издательство')
    num_pages = models.IntegerField(verbose_name='Кол-во страниц')
    num_copies = models.IntegerField(verbose_name='Количество экземпляров в библиотеке')

    def __str__(self):
        return self.title


class Visitor(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='ФИО')
    phone = models.CharField(max_length=15, verbose_name='Телефон')

    def __str__(self):
        return self.full_name


class VisitorCard(models.Model):
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE, verbose_name='Посетитель')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name='Книга')
    borrowed_date = models.DateField(verbose_name='Дата выдачи')
    returned_date = models.DateField(null=True, blank=True, verbose_name='Дата возврата')
