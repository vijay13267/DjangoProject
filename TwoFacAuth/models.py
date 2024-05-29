from django.db import models

# Create your models here.
from django.db import models

class OTP(models.Model):
    email = models.EmailField(unique=True)
    otp = models.CharField(max_length=6)
    verified = models.BooleanField(default=False)
