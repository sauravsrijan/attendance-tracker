from django.shortcuts import get_object_or_404, render
from .models import Student, AttendanceTracker
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic


class IndexView(generic.ListView):
    template_name = 'core/index.html'

    def get_queryset(self):
        return Student.objects.all()[:10]
