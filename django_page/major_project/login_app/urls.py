from django.contrib import admin
from django.urls import path
from . import views

# urlpatterns = [
#     path('', views.Home, name='home'),
#     path('register/', views.RegisterView, name='register'),
#     path('login/', views.LoginView, name='login'),
#     path('logout/',views.LogoutView, name='logout' )
# ]

urlpatterns = [
    path('', views.Home, name='home'),
    path('register/', views.RegisterView, name='register'),
    path('login/', views.LoginView, name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('doctors_details/', views.DoctorsDetails, name='doctors_details'),
    path('hospitals/', views.Hospitals, name='hospitals'),
    path('upload_image/', views.UploadImage, name='upload_image'),
]
