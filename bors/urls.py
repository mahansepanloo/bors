from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('',views.Sod.as_view()),
    path('profile',views.ShowKarbar.as_view()),
    path('best', views.Best.as_view())

]
