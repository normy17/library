from datetime import date

from django.db.models import Count, Q
from django.shortcuts import render, redirect, get_object_or_404

from web.forms import *
from web.models import *


def main_view(request):
    return render(request, 'main.html')


def books_view(request):
    books = Book.objects.all()

    query = request.GET.get('q')
    sort_by = request.GET.get('sort')

    if query:
        books = Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query) | Q(publisher__icontains=query)
        )

    if sort_by == 'title':
        books = books.order_by('title')
    elif sort_by == 'author':
        books = books.order_by('author')
    elif sort_by == 'copies':
        books = books.order_by('num_copies')

    return render(request, 'books.html', {'books': books})


def add_book_view(request):
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('books')
    return render(request, 'add_book.html', {'form': form})


def edit_book_view(request, id):
    book = get_object_or_404(Book, id=id)
    form = BookForm(instance=book)
    if request.method == 'POST':
        form = BookForm(data=request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books')
    return render(request, 'add_book.html', {'form': form})


def delete_book_view(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect('books')


def visitors_view(request):
    visitors = Visitor.objects.all()
    return render(request, 'visitors.html', {'visitors': visitors})


def add_visitor_view(request):
    form = VisitorForm()
    if request.method == 'POST':
        form = VisitorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('visitors')
    return render(request, 'add_visitor.html', {'form': form})


def edit_visitor_view(request, id):
    visitor = get_object_or_404(Visitor, id=id)
    form = VisitorForm(instance=visitor)
    if request.method == 'POST':
        form = VisitorForm(data=request.POST, instance=visitor)
        if form.is_valid():
            form.save()
            return redirect('visitors')
    return render(request, 'add_visitor.html', {'form': form})


def cards_view(request):
    books = Book.objects.filter(num_copies__gt=0)
    return render(request, 'cards.html', {'books': books})


def create_card_view(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    form = CardForm()
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.book = book
            card.save()
            book.num_copies -= 1
            book.save()
        return redirect('cards')
    return render(request, 'create_card.html', {'form': form})


def close_card_view(request):
    open_cards = VisitorCard.objects.filter(returned_date=None)
    close_cards = VisitorCard.objects.filter(returned_date__isnull=False)
    return render(request, 'close_card.html', {'open_cards': open_cards, 'close_cards': close_cards})


def close_card_2_view(request, id):
    card = get_object_or_404(VisitorCard, id=id)
    card.returned_date = date.today()
    card.save()
    book = card.book
    book.num_copies += 1
    book.save()
    return redirect('close_card')


def statistic_view(request):
    most_common_books = Book.objects.annotate(num=Count('visitorcard')).order_by('-num')[:5]
    most_active_visitors = Visitor.objects.annotate(num=Count('visitorcard')).order_by('-num')[:5]
    return render(request, 'statistic.html', {'books': most_common_books, 'visitors': most_active_visitors})