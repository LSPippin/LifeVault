from django.urls import path
from . import views

urlpatterns = [
    path('', views.pet_list, name='pet_list'),
    path('add/', views.pet_create, name='pet_create'),
    path('<int:pk>/appointment/add/', views.appointment_create, name='appointment_create'),
    path('<int:pk>/medication/add/', views.medication_create, name='medication_create'),
    path('<int:pk>/vaccine/add/', views.vaccine_create, name='vaccine_create'),
    path('<int:pk>/edit/', views.pet_edit, name='pet_edit'),
    path('<int:pk>/delete/', views.pet_delete, name='pet_delete'),
    path('<int:pk>/', views.pet_detail, name='pet_detail'),
]
