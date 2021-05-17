from django.contrib import admin
from .models import PublicProfile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

class PublicProfileInline(admin.StackedInline):
    model = PublicProfile
    can_delete = False
    verbose_name_plural = 'PublicProfile'

class UserAdmin(BaseUserAdmin):
    inlines = (PublicProfileInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)