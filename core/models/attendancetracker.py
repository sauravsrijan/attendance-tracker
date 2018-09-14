from django.db import models
from datetime import datetime
from .student import Student


class AttendanceTracker(models.Model):
    '''
    Contains attendance tracker fields.
    '''
    roll_number = models.ForeignKey(Student, related_name='roll',
                                    on_delete=models.CASCADE)
    working_days = models.IntegerField(default=0)
    present_classes = models.IntegerField(default=0)
    percentage = models.FloatField()

    def __str__(self):
        return '{}'.format(self.roll_number)

    @property
    def get_percentage(self):
        if self.working_days == 0:
            return 0.00
        else:
            percent = (self.present_classes/self.working_days)*100
            return percent

    def save(self, *args, **kwargs):
        self.percentage = self.get_percentage
        super(AttendanceTracker, self).save(*args, **kwargs)

    def get_absolute_url(self):
        #To be defined
        pass
