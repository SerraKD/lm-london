from django.shortcuts import render
from django.utils.translation import gettext as _   # translation function


def home(request):
    context = {'title': _("Home")}
    return render(request, 'main/home.html', context)


def about(request):
    context = {'title': _("About Us")}
    return render(request, 'main/about.html', context)


def services(request):
    context = {'title': _("Our Services")}
    return render(request, 'main/services.html', context)


def staircase(request):
    context = {'title': _("Staircase Design")}
    return render(request, 'main/staircase.html', context)


def gallery(request):
    context = {'title': _("Gallery")}
    return render(request, 'main/gallery.html', context)


def faq(request):
    context = {'title': _("Frequently Asked Questions")}
    return render(request, 'main/faq.html', context)


def contact(request):
    context = {'title': _("Contact Us")}
    return render(request, 'main/contact.html', context)
