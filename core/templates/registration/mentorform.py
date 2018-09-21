from core.models.mentor import Mentor
from django import forms
from django.contrib.auth.forms import UserCreationForm


class MentorForm(UserCreationForm):
    COURSE_LIST = (
        ('WEB', 'Web Development'),
        ('NTWRK', 'Networking'),
        ('ML', 'Machine Learning'),
        ('DROID', 'Android'),
        )
    SEX_TYPES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
        )

    name = forms.CharField(max_length=100, required=True)
    roll = forms.CharField(max_length=10, required=True)
    domain = forms.ChoiceField(choices=COURSE_LIST)
    phone = forms.CharField(max_length=10)
    sex= forms.ChoiceField(choices=SEX_TYPES)

    def Save(self, commit=True):
        if not commit:
            raise NotImplementedError(
                "Can't create User and UserProfile without database save")
        user = super(UserCreateForm, self).save(commit=True)
        mentor = Mentor(user=user, full_name=self.cleaned_data['name'],
            roll_number=self.cleaned_data['roll'], domain=self.cleaned_data['domain'],
            phone=self.cleaned_data['phone'], sex=self.cleaned_data['sex'])
        mentor.save()
        return user, mentor
