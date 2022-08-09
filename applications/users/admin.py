from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

# Registrar el modelo de usuario en el admin
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    pass