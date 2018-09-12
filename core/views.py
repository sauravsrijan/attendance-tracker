from django.shortcuts import get_object_or_404, render
from core.models.student import Student
from core.models.attendancetracker import AttendanceTracker
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'core/index.html'
    context_object_name = 'student_list'

    def get_queryset(self):
        return Student.objects.all()
