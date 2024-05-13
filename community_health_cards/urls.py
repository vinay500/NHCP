from django.urls import path
from . import views


urlpatterns = [
    path('buy_health_card', views.buy_health_card, name = 'buy_health_card'),
    path('assign_membership_card', views.assign_membership_card, name = 'assign_membership_card'),
]