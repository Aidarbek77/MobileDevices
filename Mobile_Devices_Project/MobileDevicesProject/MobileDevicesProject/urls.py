from django.urls import path
from . import views

urlpatterns = [
    path('', views.device_list, name='device_list'),
    path('category/', views.device_list_by_category, name='device_list_by_category'),
    path('<int:device_id>/', views.device_detail, name='device_detail'),
]
