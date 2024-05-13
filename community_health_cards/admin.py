from django.contrib import admin
from .models import MembershipCard, MembershipCardRegistrations

# Register your models here.
admin.site.register(MembershipCard)
admin.site.register(MembershipCardRegistrations)