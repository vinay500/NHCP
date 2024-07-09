from django.urls import path
from . import views


urlpatterns = [
    path('home_care_services/', views.home_care_services, name = 'home_care_services'),
    path('book_home_care_service/<str:service_name>', views.book_home_care_service, name = 'book_home_care_service'),
    # don't remove '/' from the end 
    path('booked_services/',views.view_booked_services,name="booked_services")
]