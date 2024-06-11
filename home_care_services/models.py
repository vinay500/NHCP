from django.db import models
from authentication.models import CustomUser, CountryDialCodes


# Create your models here.
class Services(models.Model):
    service_name = models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.service_name



class ServiceRegistrations(models.Model):
    user = models.ForeignKey(CustomUser,  on_delete = models.CASCADE)
    service = models.ForeignKey(Services, on_delete = models.CASCADE)
    name = models.CharField(max_length=30, null=True)
    email = models.EmailField(null=True)
    mobile_number = models.PositiveBigIntegerField(null=True)
    country = models.ForeignKey(CountryDialCodes, null=True, on_delete=models.PROTECT)
    gender = models.CharField(max_length=7, null=True)
    pin_code = models.IntegerField(null=True)
    city = models.CharField(max_length=25, null=True)
    state =  models.CharField(max_length=25, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.user.email + " - " + self.service.service_name+" - " + str(self.created_at)
