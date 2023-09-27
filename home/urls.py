from django.contrib import admin
from django.urls import path

from . import views as v

urlpatterns = [
    path('',v.home),
    path('contact',v.contact),
    path('company',v.company),
    path('careers',v.career),
    path('privacy',v.privacy),
]
