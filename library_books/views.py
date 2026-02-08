from django.shortcuts import render, get_object_or_404
from .models import Book

# View to display all books

def book_list(request):

    books = Book.objects.all()
    return render(request, "library_books/book_list.html", {"books": books})

# View to display details of a single book

def book_detail(request, pk):

    # Get book by primary key id
    
    book = get_object_or_404(Book, pk=pk) 
    return render(request, "library_books/book_detail.html", {"book": book})