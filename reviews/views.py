from django.shortcuts import render

def index(request):
    return render(request, "reviews/base.html")

def book_search(request):
    search = request.GET['search']
    return render(request, "reviews/book-search.html", {'search': search})