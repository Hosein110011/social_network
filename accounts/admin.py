from django.contrib import admin

from .models import Profile, Country



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    fields = ('user', 'phone_number', 'country', 'avatar')

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    fields = ('name', 'abbr', 'is_active')