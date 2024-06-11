from django.urls import path, include
from rest_framework import routers
from . import views

# Initialize the default router for DRF viewsets
router = routers.DefaultRouter()
router.register(r'contacts', views.ContactListView)
router.register(r'appinfo', views.AppInfoView)
router.register(r'profile', views.ProfileView)
router.register(r'register', views.RegisterView)
router.register(r'login', views.LoginView)

# Define the urlpatterns list and include both the router URLs and custom URLs
urlpatterns = [
    path('', views.phonebook, name='phonebook'),
    path('home/', views.phonebook, name='home'),  # Added home URL pattern
    path('add/', views.add_contact, name='add_contact'),
    path('edit/<int:pk>/', views.edit_contact, name='edit_contact'),
    path('delete_contact/<int:pk>/', views.delete_contact, name='delete_contact'),
]

# Add the router URLs to the urlpatterns
urlpatterns += router.urls
