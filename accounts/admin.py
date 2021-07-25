from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = ['email','first_name','last_name','is_active','date_joined']
    fieldsets = ()
    filter_horizontal = ()
    readonly_fields = ('last_login', 'date_joined')
    list_display_links = ('email', 'first_name', 'last_name')
    list_filter = ()
    ordering = ('-date_joined',)
admin.site.register(Account,AccountAdmin)
