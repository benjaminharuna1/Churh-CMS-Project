from django.contrib import admin
from .models import *
# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Member._meta.get_fields()]


class Sub_GroupAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Sub_Group._meta.get_fields()]

    
class DepartmentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Department._meta.get_fields()]

    
class DisciplerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Discipler._meta.get_fields()]
    

admin.site.register(Member, MemberAdmin)
admin.site.register(Sub_Group, Sub_GroupAdmin)
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Discipler, DisciplerAdmin)
