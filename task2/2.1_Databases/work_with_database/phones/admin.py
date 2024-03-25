from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Phone
# Register your models here.

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    pass