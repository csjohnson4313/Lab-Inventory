from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name ='dashboard-index'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('admin/', views.admin, name='admin'),
    path('add/<int:pk>/', views.add_quantity, name='add_quantity'),
    path('remove/<int:pk>/', views.remove_quantity, name='remove_quantity'),
    path('delete-custom-item/<int:pk>/', views.delete_custom_item, name='delete_custom_item'),
    path('equipment/', views.equipment_page, name='equipment_page'),
    path('equipment/checkout/', views.checkout_equipment, name='checkout_equipment'),
    path('equipment/checkin/<int:pk>/', views.checkin_equipment, name='checkin_equipment'),
]