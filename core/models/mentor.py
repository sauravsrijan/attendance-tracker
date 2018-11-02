from datetime import datetime
from django.contrib.auth.models import User, Permission
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver



class Mentor(models.Model):
    '''
    Contains basic Mentor fields.
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

    #general
    user = models.OneToOneField(
        User, related_name='mentor', on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=10, unique=True)
    domain = models.CharField(max_length=15, choices=COURSE_LIST)
    phone = models.CharField(max_length=10, blank=True)
    sex = models.CharField(
        max_length=1, choices=SEX_TYPES, blank=True, null=True)


    def __str__(self):
        return self.user.username

    @property
    def email(self):
        return self.roll_number+'@kiit.ac.in'

    @receiver(post_save, sender=User)
    def create_mentor(sender, instance, created, **kwargs):
        if created:
            Mentor.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_mentor(sender, instance, **kwargs):
        instance.mentor.save()
