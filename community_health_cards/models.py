from django.db import models
from authentication.models import CustomUser

# Create your models here.
class MembershipCard(models.Model):
    
    CARD_TYPES = ( 
        ("Basic", "Basic"), 
        ("Essential", "Essential"), 
        ("Privilage", "Privilage"), 
        ("Vip", "Vip"), 
    ) 
    type = models.CharField(max_length=15, choices=CARD_TYPES)
    card_fee = models.IntegerField()
    waiting_period = models.IntegerField()
    preventive_health_check_up = models.IntegerField()
    free_doctor_consultation = models.IntegerField()
    pharmacy_discount = models.IntegerField()
    lab_radiology_discount = models.IntegerField()
    personal_accident_insurance = models.DecimalField(max_digits=8, decimal_places=2)
    lab_radiology_wallet = models.DecimalField(max_digits=6, decimal_places=2)
    members_covered = models.IntegerField()


    def __str__(self):
        return self.type
    


class MembershipCardRegistrations(models.Model):
    user = models.ForeignKey(CustomUser,  on_delete = models.CASCADE)
    card = models.OneToOneField(MembershipCard, on_delete = models.CASCADE)

    def __str__(self):
        return self.card.type+" "+self.user.username