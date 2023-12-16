from django.db import models
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, null=False, blank=False, unique=True)
    store_id = models.CharField(max_length=250)
    daily_gold_received = models.DateField(null=True)
    is_verified = models.BooleanField(default=False)
    idfa = models.CharField(max_length=250)
    aaid = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def create_token(self) -> Token:
        return Token.objects.create(user=self)

    def __str__(self) -> str:
        return f"username: {self.username}"

    def save(self, *args, **kwargs):
        is_new = self.id is None
        super(User, self).save(*args, **kwargs)
