from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'bio', 'birthdate', 'image', 'isCandit')
    list_filter = ('is_active', 'is_staff', 'isCandit')
    search_fields = ('username', 'email', 'first_name', 'last_name')

CustomUser = get_user_model()
admin.site.register(CustomUser, CustomUserAdmin)


