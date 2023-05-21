from django.shortcuts import render
from books.models import Book

def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {'books': books}
    return render(request, template, context)


def books_date(request, pub_date):
    template = 'books/books_list.html'
    books_ = Book.objects.all()
    print(books_.query)
    books = [book for book in books_ if book.pub_date.strftime('%Y-%m-%d') == pub_date]
    context = {'books': books}
    return render(request, template, context)
