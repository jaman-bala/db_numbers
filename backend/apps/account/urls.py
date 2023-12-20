from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import sign_in, error


urlpatterns = [
    path("", sign_in, name="sign_in"),
    path("error/", error, name="error"),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]