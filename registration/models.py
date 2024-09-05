from django.contrib.auth.models import AbstractUser
from django.db import models
import random
import string


class CustomUser(AbstractUser):
    is_active = models.BooleanField(default=False)

    def generate_confirmation_code(self):
        code = ''.join(random.choices(string.digits, k=6))
        ConfirmationCode.objects.create(user=self, code=code)
        return code


class ConfirmationCode(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='confirmation_code')
    code = models.CharField(max_length=6)

    def __str__(self):
        return f"Confirmation code for {self.user.username}"
