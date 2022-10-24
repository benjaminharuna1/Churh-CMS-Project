from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import *

# Register your models here.
class MembershipAdmin(admin.ModelAdmin):
    search_fields = ['id', 'first_name', 'last_name', 'age']
    list_display = [field.name for field in Membership._meta.get_fields()]


admin.site.register (Membership, MembershipAdmin)