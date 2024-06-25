from django.urls import path
from . import views


urlpatterns = [
    path('health_cards', views.view_health_cards, name = 'view_health_cards'),
    path('buy_health_card/<str:card_type>', views.buy_health_card, name = 'buy_health_card'),
    path('assign_membership_card', views.assign_membership_card, name = 'assign_membership_card'),
    # path('assign_membership_card', views.assign_membership_card, name = 'assign_membership_card'),
]