from django.urls import path
from . import views

urlpatterns = [
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    path('category/<slug:slug>/add/', views.record_create, name='record_create'),
    path('record/<int:pk>/edit/', views.record_edit, name='record_edit'),
    path('record/<int:pk>/delete/', views.record_delete, name='record_delete'),
]
