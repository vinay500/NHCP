from django.contrib import admin
from .models import Services, ServiceRegistrations


# Register your models here.
class ServiceRegistrationsAdmin(admin.ModelAdmin):
    # list_display = ('created_at',)  # Add created_at here
    readonly_fields = ('created_at',)

admin.site.register(Services)
admin.site.register(ServiceRegistrations, ServiceRegistrationsAdmin)
