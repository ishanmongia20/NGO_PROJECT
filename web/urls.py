from django.contrib import admin
from django.urls import path
from web import views

urlpatterns = [
    path('',views.index,name='web'),
    path('donate',views.donate,name='donate'),
    path('success',views.success,name='success')
]
