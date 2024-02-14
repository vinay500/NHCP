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
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, password, **extra_fields)


class CountryDialCodes(models.Model):
    country_name = models.CharField(max_length=30)
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
    # is_mail_verified = 
    phone_number = models.PositiveBigIntegerField()
    country = models.ForeignKey(CountryDialCodes, on_delete=models.PROTECT)
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
    token = models.TextField( unique=True)

    def __str__(self):
        return self.user.email
    




