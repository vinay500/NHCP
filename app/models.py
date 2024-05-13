from django.db import models
from authentication.models import CustomUser


# Create your models here.
class Program(models.Model):
    program_name = models.CharField(max_length=40)

    def __str__(self):
        return self.program_name


class UsersRegistered(models.Model):
    program = models.ForeignKey(Program, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username+" "+self.program.program_name


