from django.shortcuts import get_object_or_404, render, redirect
from core.models.student import Student
from core.models.attendancetracker import AttendanceTracker
from core.templates.registration.mentorform import MentorForm
from django.contrib.auth import authenticate, login
from django.views import generic


def IndexView(request):
    return render(request, 'core/index.html')

def SignUp(request):
    if request.method == 'POST':
        form = MentorForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            # login(request, user)
            return redirect('/')
    else:
        form = MentorForm()

    return render(request, 'registration/signup.html', {'form': form})

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


