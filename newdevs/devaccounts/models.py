# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from .managers import CustomUserManager

# class AnonymousUserResume(models.Model):
#     resume = models.FileField()

class DevUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    # resume = models.FileField()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'Developer Account'
        verbose_name_plural = 'Developer Accounts'

    def __str__(self):
        return self.email

class EmployerAccount(DevUser):
    company_name = models.CharField(max_length=200)
    job_description = models.TextField(max_length=200)

    class Meta:
        verbose_name = 'Employer Account'
        verbose_name_plural = 'Employer Accounts'


    def __str__(self):
        return self.company_name

# class EmployerAccount(AbstractUser):
#     username = None
#     email = models.EmailField(_('email address'), unique=True)
    
#     # resume = models.FileField()
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

#     objects = CustomUserManager()

#     def __str__(self):
#         return self.email

# def Employers(AbstractUser):
#     email = models.EmailField(_('email address'), unique=True)
#     job_position = models.FileField()
#     text_field =  models.TextField()
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []

# class DevUser(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     firstname  = models.CharField(max_length=200)
#     lastname  = models.CharField(max_length=200)

#     # image =  field_name = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
#     # bio = models.TextField(max_length=500, blank=True)
#     # location = models.CharField(max_length=30, blank=True)
#     # birth_date = models.DateField(null=True, blank=True)

# class DevForm(ModelForm):

#     class Meta:
#         model = DevUser
#         fields = ['user']
