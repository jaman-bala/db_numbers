from django.urls import path
from . import views


urlpatterns = [
    path("", views.get_index, name='main'),
    path("category_regions/", views.get_category_region, name='category_regions'),
]
