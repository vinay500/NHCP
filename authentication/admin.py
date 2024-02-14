from django.contrib import admin
from .models import CustomUser, CountryDialCodes


# Register your models here.
admin.site.register(CustomUser)
admin.site.register(CountryDialCodes)