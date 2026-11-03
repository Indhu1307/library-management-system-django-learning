from django.shortcuts import render,get_object_or_404
from .models import Book

def home(request):
    books = Book.objects.all()

    search_query = request.GET.get("search", "")
    category = request.GET.get("category", "")

    if search_query:
        books = books.filter(title__icontains=search_query)

    if category:
        books = books.filter(category=category)

    categories = Book.objects.values_list(
        'category', flat=True
    ).distinct()

    return render(request, 'myapp/home.html', {
        'books': books,
        'categories': categories,
       
    })


def book_detail(request,book_id):
    book=get_object_or_404(Book,id=book_id)
    return render(
        request, 'myapp/book_detail.html',{'book':book} 
    )
