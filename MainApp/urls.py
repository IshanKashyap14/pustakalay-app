"""
URL configuration for LivingLibrary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from .views import AllFuncs
from django.conf import settings
from django.conf.urls.static import static

all_funcs = AllFuncs()


urlpatterns = [
    path('',all_funcs.home_page),
    path('main',all_funcs.main_page),
    path('newbook',all_funcs.newbook,name='newbook'),
    path('bookcreated',all_funcs.bookscreated),
    path('questions',all_funcs.questions),
    path('qcreate',all_funcs.qcreate),
    path('book',all_funcs.bookpage),
    path('bookerror',all_funcs.bookerror),
    path('borrowpage',all_funcs.borrowpage),
    path('answerit',all_funcs.answerit),
    path('readbook',all_funcs.readbook),
    path('payment',all_funcs.payment_page),
    path('paydone',all_funcs.paydone_page),
    path('returnbook',all_funcs.returnbook)
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
