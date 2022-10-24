from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
import os, random


def filename_ext(filepath):
    file_base = os.path.basename(filepath)
    filename, ext = os.path.splitext(file_base)
    return filename, ext


def upload_image_path(instance, filename):
    new_filename = random.randint(1, 9498594795)
    name, ext = filename_ext(filename)
    final_filename = "{new_filename}{ext}".format(new_filename=new_filename, ext=ext)
    return "pictures/{new_filename}/{final_filename}".format(new_filename=new_filename, final_filename=final_filename)


class Sub_Group(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    leader = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    leader = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Discipler(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class MembershipManager(models.Manager):
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

    def new_believer_school(self):
        # return self.get_queryset().filter(new_believer_school=True)
        return self.active().filter(new_believer_school=True)

    def pays_tithe(self):
        # return self.get_queryset().filter(pays_tithe=True)
        return self.active().filter(pays_tithe=True)

    def working(self):
        # return self.get_queryset().filter(working=True)
        return self.active().filter(working=True)

    def schooling(self):
        # return self.get_queryset().filter(schooling=True)
        return self.active().filter(schooling=True)


class Membership(models.Model):
    name = models.CharField(max_length=255)
    active = models.BooleanField()
    Discipler = models.ForeignKey(Discipler, on_delete=models.CASCADE, null=True, blank=True)
    sub_group = models.ForeignKey(Sub_Group, on_delete=models.CASCADE, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    telephone = PhoneNumberField(null=True, blank=True)
    location = models.CharField(max_length=255)
    fathers_name = models.CharField(max_length=255, null=True, blank=True)
    mothers_name = models.CharField(max_length=255, null=True, blank=True)
    guardians_name = models.CharField(max_length=255, null=True, blank=True)
    new_believer_school = models.BooleanField()
    pays_tithe = models.BooleanField()
    working = models.BooleanField()
    schooling = models.BooleanField()
    picture = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    objects = MembershipManager()

    def __str__(self):
        return self.name


class TestDb(models.Model):
    field = models.CharField(max_length=120)