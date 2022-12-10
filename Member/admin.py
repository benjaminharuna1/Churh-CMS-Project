from django.contrib import admin
from .models import *


class MemberSubGroupItemInline(admin.TabularInline):
    model = MemberSubGroup
    raw_id_fields = ['member'] 


class MemberCommitteeItemInline(admin.TabularInline):
    model = MemberCommittee
    raw_id_fields = ['member'] 


class EmploymentDetailsItemInline(admin.TabularInline):
    model = EmploymentDetails
    raw_id_fields = ['member'] 

    
class EducationInformationItemInline(admin.TabularInline):
    model = EducationInformation
    raw_id_fields = ['member'] 



class MemberAdmin(admin.ModelAdmin):
    search_fields = ('ID', 'first_name', 'last_name', 'other_names', 'active', 'sex', 'discipler', 'telephone', 'address', 'country', 'state_of_origin', 'lga', 'marital_status', 'spouse_name', 'next_of_kin', 'relationship_with_nok', 'number_of_children', 'address', 'date_joined', 'tribe', 'fathers_name', 'mothers_name', 'guardians_name', 'home_cell' )
    list_display = ('ID', 'first_name', 'last_name', 'other_names', 'active', 'sex', 'discipler', 'telephone', 'address', 'country', 'state_of_origin', 'lga', 'marital_status', 'spouse_name', 'next_of_kin', 'relationship_with_nok', 'number_of_children', 'address', 'date_joined', 'tribe', 'fathers_name', 'mothers_name', 'guardians_name', 'home_cell')
    list_filter = ('ID', 'first_name', 'last_name', 'other_names', 'active', 'sex', 'telephone', 'address', 'country', 'state_of_origin', 'lga', 'marital_status',    'date_joined', 'tribe',  "home_cell")
    inlines = [MemberSubGroupItemInline, MemberCommitteeItemInline, EmploymentDetailsItemInline, EducationInformationItemInline]

    
class SubGroupAdmin(admin.ModelAdmin):
    search_fields = ('name', 'leader',)
    list_display = ('name', 'description', 'leader', 'contact',)
    list_filter = ('name', 'leader',)

    
class CommitteeAdmin(admin.ModelAdmin):
    search_fields = ('name', 'leader',)
    list_display = ('name', 'description', 'leader', 'contact',)
    list_filter = ('name', 'leader',)

class HomeCellAdmin(admin.ModelAdmin):
    search_fields = ('name', 'leader',)
    list_filter = ('name', 'leader',)
    list_display = ('name', 'address', 'leader', 'contact')

class MemberSubGroupAdmin(admin.ModelAdmin):
    search_fields = ('member', 'subgroup')
    list_filter = ('member', 'subgroup')
    list_display = ('member', 'subgroup')

class MemberCommitteeAdmin(admin.ModelAdmin):
    search_fields = ('member', 'committee')
    list_filter = ('member', 'committee')
    list_display = ('member', 'committee')
    

    
class EmploymentDetailsAdmin(admin.ModelAdmin):
    search_fields = ('member',)
    list_filter = ('member',)
    list_display = ('member', 'employer_name', 'office_address', 'years_in_employment')


class EducationInformationAdmin(admin.ModelAdmin):
    search_fields = ('member',)
    list_filter = ('member','school')
    list_display = ('member', 'school', 'course', 'start_year', 'duration')



admin.site.register(Member,MemberAdmin)
admin.site.register(SubGroup, SubGroupAdmin)
admin.site.register(MemberSubGroup, MemberSubGroupAdmin)
admin.site.register(Committee, CommitteeAdmin)
admin.site.register(MemberCommittee, MemberCommitteeAdmin)
admin.site.register(HomeCell, HomeCellAdmin)
admin.site.register(EmploymentDetails, EmploymentDetailsAdmin)
admin.site.register(EducationInformation, EducationInformationAdmin)