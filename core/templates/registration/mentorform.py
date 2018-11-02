from core.models.mentor import Mentor
from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')

class MentorProfileForm(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = ('full_name', 'roll_number', 'domain', 'phone', 'sex')
