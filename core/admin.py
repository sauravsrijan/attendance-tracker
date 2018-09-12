from django.contrib import admin
from core.models.student import Student
from core.models.attendancetracker import AttendanceTracker
# Register your models here.
admin.site.register(Student)
admin.site.register(AttendanceTracker)
