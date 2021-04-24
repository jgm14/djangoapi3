"""queueapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from queueapi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('customers/<int:id>', views.CustomerView.as_view()),
    #path('customers/', views.CustomerView.as_view()),
    path('queues/<int:id>', views.QueueView.as_view()),
    path('queues/', views.QueueView.as_view()),
    path('guests/<int:id>', views.GuestView.as_view()),
    path('guests/', views.GuestView.as_view()),
    path('inqueue/<int:id>', views.InQueueView.as_view()),
    path('inqueue/', views.InQueueView.as_view()),
    path('auth/signup/', views.UsersView.as_view()),
    path('auth/signin/', views.UsersView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
