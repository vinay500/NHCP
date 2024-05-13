from django.urls import path
from . import views


urlpatterns = [
    path('save_dependent', views.save_dependent, name = 'save_dependent'),
    path('view_dependents', views.view_dependents, name = 'view_dependents'),
    path('view_dependent/<str:dep_id>', views.view_dependent, name = 'view_dependent'),
]
