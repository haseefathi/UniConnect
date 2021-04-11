from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import SiteUser


class SiteUserInline(admin.StackedInline):
    model = SiteUser
    can_delete = False
    verbose_name_plural = 'siteuser'

class UserAdmin(BaseUserAdmin):
    inlines = (SiteUserInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)