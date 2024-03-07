from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ['email', 'is_staff', 'is_admin', 'first_name', 'last_name',  'dob', 'gender', 'weight', 'height']


admin.site.register(User, UserAdmin)
