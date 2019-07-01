from django.conf.urls import url, include
from django.urls import include, path
from django.contrib import admin
from . import views

urlpatterns = [
    path('entities/', views.hello_world),
    path('entities/1/', views.Entity_list.as_view()),
]
