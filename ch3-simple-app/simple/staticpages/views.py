from django.shortcuts import render


def home_page_view(request):
    return render(request, 'staticpages/index.html')


def about_page_view(request):
    return render(request, 'staticpages/about.html')
