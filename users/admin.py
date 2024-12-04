from django.contrib import admin
from .models import User

@admin.register(User)
class YourModelAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'email', 'phone_number', 'registration_date')
    search_fields = ('username', 'email', 'phone_number')
    list_filter = ('registration_date',)
