from django.db import models


class Users(models.Moded):
    '''
    Contains basic user fields.
    '''
    COURSE_LIST = (
        ('WEB', 'Web Development'),
        ('NTWRK', 'Networking'),
        ('ML', 'Machine Learning'),
        ('DROID', 'Android'),
        )

    full_name = models.CharField(max_length=100)
    branch = models.CharField(max_length=30)
    roll_number = models.CharField(max_length=10)
    phone = models.CharField(max_length=10) #to be rechecked.
    email = models.EmailField()
    course_opted = models.CharField(choices=COURSE_LIST)
    percentage = models.ForeignKey(AttendanceTracker, related_name='users',
                                   on_delete=models.CASCADE)
    valid_till = models.DateTimeField()

    def get_absolute_url(self):
        #To be defined
        pass


class AttendanceTracker(models.Model):
    '''
    Contains attendance tracker fields.
    '''
    roll_number = models.ForeignKey(Users, related_names='roll',
                                    on_delete=models.CASCADE)
    working_days = models.IntegerField(default=0)
    present_classes = models.IntegerField(default=0)
    percentage = models.FloatField(default=0.0)

    def get_attendance(self):
        return
