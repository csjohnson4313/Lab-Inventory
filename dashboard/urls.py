from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name ='dashboard-index'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('admin/', views.admin, name='admin'),
    path('add/<int:pk>/', views.add_quantity, name='add_quantity'),
    path('remove/<int:pk>/', views.remove_quantity, name='remove_quantity'),
]