from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('companies/', views.companies, name='companies'),
    path('applications/', views.applications, name='applications'),
    path('apply-form/<int:id>/', views.apply_form, name='apply_form'),
]