from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from accounts.models import Profile
from accounts.forms import CustomUserChangeForm, CustomUserCreationForm
# Register your models here.


User = get_user_model()


class ProfileInline(admin.StackedInline):
    model = Profile


@admin.register(User)
class UserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ['username','email','email_verified','is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (
            "Additional Info",{
                "fields":("gender","email_verified","date_of_birth"),
            }
        ),
    )
    add_fieldsets = (
        (
            "Create User",{
                "classes":("wide",),
                "fields":("username","email","password1","password2"),
            }
        ),
    )
    def get_inlines(self, request, obj=None):
        if obj:
            return [ProfileInline]
        return []