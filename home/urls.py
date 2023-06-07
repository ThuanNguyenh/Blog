
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path("", views.index),
    path("contact/", views.contact, name='contact'),
    path("register/", views.register, name='register'),
    path('login/', LoginView.as_view(template_name='page/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('login/facebook/', views.FacebookLogin.as_view(), name='facebook_login'),
]