from django.urls import path
from . import views
urlpatterns = [
    #path core
    path("", views.home, name = "home"),
    path("dashboard/", views.home, name = "home"),
    path('about/', views.about, name="about"),
    path('store/', views.store, name="store"),
    path('contact/', views.contact, name="contact"),
    path('sample/', views.sample, name="sample"),
]