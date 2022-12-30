from django.contrib import admin

from core.models import Recipi
# Register your models here.
@admin.register(Recipi)
class RecipiAdmin(admin.ModelAdmin):
    list_display = ['title','user','time_minutes']
    