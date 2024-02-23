from django.contrib import admin
from .models import CustomUser, CountryDialCodes, Forgot_Password_Request


# Register your models here.
admin.site.register(CustomUser)
admin.site.register(CountryDialCodes)
admin.site.register(Forgot_Password_Request)