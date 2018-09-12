from django.db import models
from datetime import datetime


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

    joined = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(max_length=100)
    branch = models.CharField(max_length=30)
    roll_number = models.CharField(max_length=10)
    phone = models.CharField(max_length=10) #to be rechecked.
    email = models.EmailField()
    course_opted = models.CharField(max_length=15, choices=COURSE_LIST)
    valid_till = models.DateTimeField()
    is_active = models.BooleanField(default=False)
    # percentage =

    class Meta:
        ordering = ('full_name',)

    def __str__(self):
        return '{}'.format(self.roll_number)

    def get_absolute_url(self):
        #To be defined
        pass

    def set_validity(self):
        if valid_till <= datetime.now():
            is_active = True
        else:
            is_active = False

    def active_status(self):
        if is_active:
            return 'ACTIVE'
        else:
            return 'INACTIVE'



class AttendanceTracker(models.Model):
    '''
    Contains attendance tracker fields.
    '''
    roll_number = models.ForeignKey(Student, related_name='roll',
                                    on_delete=models.CASCADE)
    working_days = models.IntegerField(default=0)
    present_classes = models.IntegerField(default=0)
    percentage = models.FloatField(default=0.0)

    def __str__(self):
        return '{}'.format(self.roll_number)

    def get_attendance(self):
        if self.working_days == 0:
            return "No classes conducted yet."
        else:
            percent = (self.present_classes/self.working_days)*100
            return percent

    def get_absolute_url(self):
        #To be defined
        pass
