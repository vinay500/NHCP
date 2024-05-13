from django.db import models
from authentication.models import CustomUser, CountryDialCodes


# Create your models here.

class BeyondBordersDependents(models.Model):
    refered_by = models.ForeignKey(CustomUser, null= True,on_delete = models.CASCADE)
    # membership_id = models.CharField(max_length = )
    membership_id = models.CharField(max_length=20, unique=True, null=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=7)
    relation = models.CharField(max_length=15)
    phone_number = models.PositiveBigIntegerField()
    country = models.ForeignKey(CountryDialCodes, on_delete=models.PROTECT)
    address = models.TextField()
    current_issue_treatment_expected = models.TextField(null= True)
    health_insurance_details = models.TextField(null= True)
    image_filename = models.CharField(max_length = 60, null=True)

    
    def save(self, *args, **kwargs):
        print('in save()')
        if not self.membership_id:
            print(' in not self.membership_id')
            # Get the current number of dependents for this user to calculate the next ID suffix
            current_dependents_count = BeyondBordersDependents.objects.filter(refered_by=self.refered_by).count()
            print('current_dependents_count: ',current_dependents_count)
            # Generate the new membership ID with the format: NXP-user_id-000001
            # Increment the ID suffix based on the current_dependents_count
            new_id_suffix = current_dependents_count + 1
            self.membership_id = f"NXP-{self.refered_by.id}-{new_id_suffix:06}"
            print('self.membership_id: ',self.membership_id)
        super(BeyondBordersDependents, self).save(*args, **kwargs)


    def __str__(self):
        return self.first_name

