"""
URL configuration for steelbusiness project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns
from django.urls import path, include
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('set-language/', views.set_language, name='set_language'),
    path('', views.home, name='home'),  # Root URL pattern
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('staircase/', views.staircase, name='staircase'),
    path('gallery/', views.gallery, name='gallery'),
    path('faq/', views.faq, name='faq'),
    path('contact/', views.contact, name='contact'),
]

urlpatterns += i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
)
