from django.urls import path
from . import views

urlpatterns = [
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    path('category/<slug:slug>/add/', views.record_create, name='record_create'),
]
