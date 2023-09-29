from django.contrib import admin
from .models import User, UserManager

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id','username','email','is_verified']
