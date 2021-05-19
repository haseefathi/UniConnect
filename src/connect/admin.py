from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import PublicProfile

# Register your models here.

class PublicProfileInline(admin.StackedInline):
    model = PublicProfile
    can_delete = False
    verbose_name_plural = 'PublicProfile'

# class UserAdmin2(BaseUserAdmin):
#     inlines = (PublicProfileInline,)

# admin.site.unregister(User)
# admin.site.register(User, UserAdmin2)

