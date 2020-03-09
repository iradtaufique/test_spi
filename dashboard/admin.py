from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUser
from django.contrib.auth.models import User
from .models import UserProfile, ProjectTeam, Profile


class ProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False


class UserAdmin(BaseUser):
    inlines = [ProfileInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(ProjectTeam)
admin.site.register(Profile)

