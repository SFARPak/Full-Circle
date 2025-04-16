# pages/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('',           views.index,         name='index'),
    path('about/',     views.about,         name='about'),
    path('blog/',      views.blog,          name='blog'),
    path('blog-details/', views.blog_details, name='blog_details'),
        path('contact/', views.contact_view, name='contact'),
    path('elements/',  views.elements,      name='elements'),
    path('events/',    views.events,        name='events'),
    path('program/',   views.program,       name='program'),
    path('donate/',      views.donate,          name='donate'),
     path('support/',      views.support,          name='support'),
]
