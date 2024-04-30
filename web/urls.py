from django.urls import path, include
from .views import *


urlpatterns = [
    path('', main_view, name='main'),
    path('books/', books_view, name='books'),
    path('add_book/', add_book_view, name='add_book'),
    path('edit_book/<int:id>/', edit_book_view, name='edit_book'),
    path('delete_book/<int:id>/', delete_book_view, name='delete_book'),
    path('visitors/', visitors_view, name='visitors'),
    path('add_visitor/', add_visitor_view, name='add_visitor'),
    path('edit_visitor/<int:id>/', edit_visitor_view, name='edit_visitor'),
    path('cards/', cards_view, name='cards'),
    path('create_card/<int:book_id>/', create_card_view, name='create_card'),
    path('close_card/', close_card_view, name='close_card'),
    path('close_card/<int:id>', close_card_2_view, name='close_card_2'),
    path('statistic/', statistic_view, name='statistic')

]