from django.shortcuts import get_object_or_404, render
from core.models.student import Student
from core.models.attendancetracker import AttendanceTracker
from django.views import generic


class WebDevelopment(generic.ListView):
    template_name = 'core/webindex.html'
    context_object_name = 'student_list'

    def get_queryset(self):
        return Student.objects.filter(course_opted='WEB')

class Networking(generic.ListView):
    template_name = 'core/networkingindex.html'
    context_object_name = 'student_list'

    def get_queryset(self):
        return Student.objects.filter(course_opted='NTWRK')

class MachineLearning(generic.ListView):
    template_name = 'core/mlindex.html'
    context_object_name = 'student_list'

    def get_queryset(self):
        return Student.objects.filter(course_opted='ML')

class Android(generic.ListView):
    template_name = 'core/androidindex.html'
    context_object_name = 'student_list'

    def get_queryset(self):
        return Student.objects.filter(course_opted='DROID')
