from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index-url'),
    path('about/',views.about,name='about-url'),
    path('services/',views.services,name='services-url'),
    path('portfolio/',views.portfolio,name='portfolio-url'),
    path('team/',views.team,name='team-url'),
    path('blog/',views.blog,name='blog-url'),
    path('blogDetails/',views.blogDetails,name='blogDetails-url'),
    path('contact/',views.contact,name='contact-url'),
]

