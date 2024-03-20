from django.urls import path
from . import views


urlpatterns = [
    path("", views.get_index, name='main'),
    path('unaa/<int:unaa_id>/', views.unaa_detail, name='unaa_detail'),
    path('check_number_exists', views.check_number_exists, name='check_number_exists'),
]

