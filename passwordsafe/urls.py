from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_passwords, name='passwordsafe'),
    path('add/', views.add_password, name='addpassword'),
    path('delete/<item_id>/', views.delete_password, name='delpassword'),
]
