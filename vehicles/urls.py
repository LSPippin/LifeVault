from django.urls import path
from . import views

urlpatterns = [
    path('', views.vehicle_list, name='vehicle_list'),
    path('add/', views.vehicle_create, name='vehicle_create'),
    path('<int:pk>/maintenance/add/', views.maintenance_create, name='maintenance_create'),
    path('<int:pk>/oilchange/add/', views.oilchange_create, name='oilchange_create'),
    path('<int:pk>/edit/', views.vehicle_edit, name='vehicle_edit'),
    path('<int:pk>/delete/', views.vehicle_delete, name='vehicle_delete'),
    path('<int:pk>/', views.vehicle_detail, name='vehicle_detail'),
]
