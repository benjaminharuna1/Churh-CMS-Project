import os, random
from django.db import models
from django.forms import ValidationError
from phonenumber_field.modelfields import PhoneNumberField




# Create your models here.
def filename_ext(filepath):
    file_base = os.path.basename(filepath)
    filename, ext = os.path.splitext(file_base)
    return filename, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1, 9498594795)
    name, ext = filename_ext(filename)
    final_filename = "{new_filename}{ext}".format(new_filename=new_filename, ext=ext)
    return "pictures/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)


class Church_Info(models.Model):
    church_name = models.CharField(max_length = 255, null=True, blank=True)
    church_address = models.CharField(max_length = 255, null=True, blank = True)
    church_contact = PhoneNumberField(blank=True, null=True)
    church_logo = models.ImageField(upload_to=upload_image_path, null=True, blank=True)
    church_domain = models.URLField(max_length = 255, blank=True, null=True)
    church_email = models.EmailField(blank=True, null = True)

    def clean(self):
        if (Church_Info.objects.count() >=1 and self.pk is None):
            raise ValidationError("You can only Create one Church Profile. Please edit the current church information or contact a developer!!")
        
    
    class Meta:
        verbose_name_plural = "Church Info"
        
    def __str__(self):
        return f'{self.church_name}' + " " + " Church Profile Information"