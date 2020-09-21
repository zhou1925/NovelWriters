from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("novels_count",)
