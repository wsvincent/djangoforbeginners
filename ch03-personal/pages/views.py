from django.http import HttpResponse
from django.shortcuts import render


def home_page_view(request):
    return HttpResponse("Homepage")


def about_page_view(request):
    context = {
        "name": "Alice",
        "age": 33,  # new
    }
    return render(request, "pages/about.html", context)
