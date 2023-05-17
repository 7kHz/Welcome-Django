from django.shortcuts import render
from books.models import Book


def books_view(request):
    context = {}
    template = 'books/books_list.html'
    books = Book.objects.all()
    for book in books:
        context_ = {'book': book}
        context.update(context_)
    return render(request, template, context)
