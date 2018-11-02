from django.shortcuts import get_object_or_404, render, redirect
from core.models.student import Student
from core.models.attendancetracker import AttendanceTracker
from core.templates.registration.mentorform import UserForm, MentorProfileForm
from django.contrib.auth import authenticate, login
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.db import transaction


def IndexView(request):
    return render(request, 'core/index.html')


def SignUp(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        mentor_profile_form = MentorProfileForm(request.POST, instance=request.user.mentor)
        if user_form.is_valid() and mentor_profile_form.is_valid():
            user_form.save()
            mentor_profile_form.save()
            messages.success(request, "User successfully created")
        else:
            messages.error(request, "Correct errors")
    else:
        user_form = UserForm(instance=request.user)
        mentor_profile_form = MentorProfileForm(instance=request.user.mentor)
    return render(request, 'create_profile.html', {
        'user_form': user_form,
        'mentor_profile_form': mentor_profile_form
    })


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

# def mark_attendance(request, student_id):
#     student = get_object_or_404(Student, pk=student_id)


