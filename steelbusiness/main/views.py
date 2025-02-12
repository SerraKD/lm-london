from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html')


def about(request):
    return render(request, 'main/about.html')


def services(request):
    return render(request, 'main/services.html')


def staircase(request):
    return render(request, 'main/staircase.html')


def gallery(request):
    return render(request, 'main/gallery.html')


def faq(request):
    return render(request, 'main/faq.html')


def contact(request):
    return render(request, 'main/contact.html')
