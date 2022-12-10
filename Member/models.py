import os, random


from django.db import models
from phonenumber_field.modelfields import PhoneNumberField



def filename_ext(filepath):
    file_base = os.path.basename(filepath)
    filename, ext = os.path.splitext(file_base)
    return filename, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1, 9498594795)
    name, ext = filename_ext(filename)
    final_filename = "{new_filename}{ext}".format(new_filename=new_filename, ext=ext)
    return "pictures/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)




class Committee(models.Model):
    name = models.CharField(primary_key=True, max_length=255)
    description = models.TextField()
    leader = models.CharField(max_length=255)
    contact = PhoneNumberField(null=True, blank = True)

    def __str__(self):
        return self.name

    

class SubGroup(models.Model):
    name = models.CharField(primary_key=True, max_length=255)
    description = models.TextField()
    leader = models.CharField(max_length=255)
    contact = PhoneNumberField(null=True, blank = True)


    def __str__(self):
        return self.name
    

class HomeCell(models.Model):
    name = models.CharField(primary_key=True, max_length=255)
    address = models.CharField(max_length=255)
    leader = models.CharField(max_length=255)
    contact = PhoneNumberField(null=True, blank=True)

    def __str__(self):
        return self.name
     
        
class MemberManager(models.Manager):
    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None

    def active(self):
        qs = self.get_queryset().filter(active=True)
        return qs

    def deleted(self):
        return self.get_queryset().filter(active=False)

   

class Member(models.Model):
    ID = models.AutoField(primary_key=True)
    first_name = models.CharField('First Name', max_length=255)
    last_name = models.CharField('Last Name', max_length=255)
    other_names = models.CharField('Other Names', max_length=255, blank=True, null=True)
    active = models.BooleanField()


    MALE = 'M'
    FEMALE = 'F'
    STATUS = [
            (MALE, 'Male'),
            (FEMALE, 'Female'),
            ]
    sex = models.CharField(max_length=1, choices=STATUS, default=MALE)


    discipler = models.CharField(max_length=255, blank=True, null=True)
    telephone = PhoneNumberField(null=True, blank=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    state_of_origin = models.CharField(max_length=255, blank=True, null=True)
    lga = models.CharField('Local Governemnt Area', max_length=255, blank=True, null=True)


    SINGLE = 'S'
    MARRIED = 'M'
    DIVORCED = 'D'
    WIDOWED = 'W'
    STATUS = [
            (SINGLE, 'Single'),
            (MARRIED, 'Married'),
            (DIVORCED, 'Divorced'),
            (WIDOWED, 'Widowed')
            ]
    marital_status = models.CharField(max_length=1, choices=STATUS, default=SINGLE)

    spouse_name = models.CharField('Spouse Name (Leave Blank if Single)', max_length=255, blank=True, null=True)
    next_of_kin = models.CharField('Next of Kin', max_length = 255, blank=True, null=True)
    relationship_with_nok = models.CharField('Relationship with Next of Kin', max_length=255, blank=True, null=True)
    number_of_children= models.PositiveIntegerField('Number of children', blank=True, null=True)
    address = models.CharField('Residential Address', max_length=255, blank=True, null=True)
    
        
    
    date_joined = models.DateField(null=True, blank=True)



    tribe = models.CharField(max_length=255, blank=True, null=True)
    fathers_name = models.CharField(max_length=255, null=True, blank=True)
    mothers_name = models.CharField(max_length=255, null=True, blank=True)
    guardians_name = models.CharField(max_length=255, null=True, blank=True)
    home_cell = models.ForeignKey(HomeCell, on_delete=models.PROTECT)
    
    
    # uploads
    picture = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    
    signature = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    
  
    objects = MemberManager()

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.other_names

 

class MemberCommittee(models.Model):
    member = models.ForeignKey(Member, on_delete=models.PROTECT)
    committee = models.ForeignKey(Committee, on_delete=models.PROTECT)


class MemberSubGroup(models.Model):
    member = models.ForeignKey(Member, on_delete=models.PROTECT, db_constraint=False)
    subgroup = models.ForeignKey(SubGroup, on_delete=models.PROTECT, db_constraint=False)    



class EmploymentDetails(models.Model):
    member = models.ForeignKey(Member, on_delete=models.PROTECT)
    employer_name = models.CharField(primary_key=True, max_length=255)
    office_address = models.CharField(max_length=255, null=True, blank=True)
    years_in_employment = models.PositiveIntegerField(blank=True, null=True)


class EducationInformation(models.Model):
    member = models.ForeignKey(Member, on_delete=models.PROTECT)
    school = models.CharField(primary_key=True, max_length=255)
    course = models.CharField(max_length=255, null=True, blank=True)
    start_year = models.PositiveIntegerField(blank=True, null=True)
    duration = models.PositiveIntegerField(blank = True, null = True)


class TestDb(models.Model):
    field = models.CharField(max_length=120)