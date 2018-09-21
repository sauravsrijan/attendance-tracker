from datetime import timedelta
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone



class Student(models.Model):
    '''
    Contains basic user fields.
    '''
    COURSE_LIST = (
        ('WEB', 'Web Development'),
        ('NTWRK', 'Networking'),
        ('ML', 'Machine Learning'),
        ('DROID', 'Android'),
        )
    SEX_TYPES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
        )

    # user = models.OneToOneField(
    #     User, related_name='student', default=None, on_delete=models.CASCADE) # To be added in later update.
    # is_admin = models.BooleanField(default=False)  # To be added in later update
    full_name = models.CharField(max_length=100)
    branch = models.CharField(max_length=30)
    roll_number = models.CharField(max_length=10, unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    sex = models.CharField(
        max_length=1, choices=SEX_TYPES, blank=True, null=True)
    course_opted = models.CharField(max_length=15, choices=COURSE_LIST)
    active_from = models.DateTimeField(auto_now_add=True)
    expiry = models.IntegerField(default=365)  # One Year Validity

    class Meta:
        ordering = ('full_name',)

    def __str__(self):
        return '{}'.format(self.roll_number)

    # def get_absolute_url(self):
    #     #To be defined
    #     pass

    @property
    def email(self):
        return self.roll_number+'@kiit.ac.in'


    @property
    def is_active(self):
        active_till = self.active_from+timedelta(self.expiry)
        if active_till >= timezone.now():
            return True
        else:
            return False
