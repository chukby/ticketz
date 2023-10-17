from django.urls import path
from . import views

urlpatterns = [
    path('register-client/', views.register_client, name='register_client'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]
