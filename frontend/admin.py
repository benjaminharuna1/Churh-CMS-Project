from django.contrib import admin
from frontend . models import *

# Register your models here.

class Church_InfoAdmin(admin.ModelAdmin):
    ist_display = ('church_name', 'church_address', 'church_contact', 'church_logo', 'church_domain')
    inlines = []


admin.site.register(Church_Info,Church_InfoAdmin)
