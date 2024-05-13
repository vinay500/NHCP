from django.db import models
from django.contrib.auth.models import User 
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone
from django.db import models

    

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        print("user.phone_number: ",user.phone_number)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        phone_number = None
        return self.create_user(email, password, phone_number=phone_number, **extra_fields)


class CountryDialCodes(models.Model):
    country_name = models.CharField(max_length=40)
    country_short_form = models.CharField(max_length=5)
    country_dial_code = models. PositiveSmallIntegerField()

    def __str__(self) -> str:
        return self.country_name
    
    class Meta:
        ordering = ('country_name',)


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    # removing unique constraint for username
    username = models.CharField(max_length=150, unique=False)
    phone_number = models.PositiveBigIntegerField()
    country = models.ForeignKey(CountryDialCodes, on_delete=models.PROTECT)
    # null=True is added because when user is created while signup then date of birth, gender and foreign address are not taken
    # date of birth, gender and foreign address are being taken while adding dependent
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(max_length=7, null=True)
    foreign_address = models.TextField()
    is_mail_verified = models.BooleanField(default=False)
    
    # country = models.CharField(max_length=30)
    # country_short_form = models.CharField(max_length=5)
    # phone_number = models.PositiveBigIntegerField()
    # dial_code = models. PositiveSmallIntegerField()


    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    #email is requied while creating superuser
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    

class Forgot_Password_Request(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=timezone.now)
    token = models.TextField(unique=True)

    def __str__(self):
        return self.user.email
    




