from django.urls import path
from . import views

urlpatterns = [
    path('first_app/', views.home, name = "homepage"),
    path('first_app/about/', views.about, name = 'aboutpage'),
    path('first_app/form/', views.submit_form, name='formpage'),
    path('first_app/django_form/', views.PasswordValidation, name='django_form'),
]