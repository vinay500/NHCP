from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.signup, name = 'signup'),
    path('signin/', views.signin, name = 'signin'),
    path('signin/<str:reset_password_msg>/', views.signin, name = 'signin'),
    path('verify_mail/<str:token>/', views.verify_mail, name='verify_mail'),
    # path('country_dial_codes', views.save_country_data , name = 'country_dial_codes'),
    path('forgot_password_page/', views.forgot_password_page, name = 'forgot_password_page'),
    # forgot password page with error message 
    path('forgot_password_page/<str:error_msg>/', views.forgot_password_page, name = 'forgot_password_page'),
    path('reset_password/<str:token>', views.reset_password, name = 'reset_password'),
    path('reset_password_invalid_token/', views.reset_password_invalid_token , name = 'reset_password_invalid_token'),
    path('signout/', views.signout , name = 'signout'),
]


