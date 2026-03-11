from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio/<slug:slug>/', views.portfolio_detail, name='portfolio-detail'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
]