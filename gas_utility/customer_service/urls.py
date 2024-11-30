# customer_service/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page, landing or dashboard
    path('login/', views.login_view, name='login'),  # Login page
    path('signup/', views.signup, name='signup'),  # Signup page
    path('service_requests/', views.service_requests, name='service_requests'),  # User service requests
    path('create_service_request/', views.create_service_request, name='create_service_request'),  # Create service request
    path('service_request/<int:request_id>/', views.service_request_detail, name='service_request_detail'),  # Service request details
    path('update_service_request/<int:request_id>/', views.update_service_request, name='update_service_request'),  # Update service request
]
