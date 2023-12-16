from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from rest_framework.authtoken.admin import TokenAdmin

from .models import User

TokenAdmin.raw_id_fields = ['user']


@admin.register(User)
class UserAdmin(UserAdmin):
    list_filter = ['is_staff', 'is_superuser', 'created_at', 'updated_at']
