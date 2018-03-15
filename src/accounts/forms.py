from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import User,Student,Teacher,Grade


class StudentSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        return user


class TeacherSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic   
    def save(self, commit=False):
        user = super().save(commit=False)
        user.is_teacher = True
        user.save()
        teacher = Teacher.objects.create(user=user)
        return user



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email','avatar','adresse','birth_location','birth_day')



class TeacherForm(forms.ModelForm):
    classroom = forms.ModelMultipleChoiceField(
        queryset=Grade.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
        )
    class Meta:
        model = Teacher
        fields = ('reciption', 'module','classroom')

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('classroom',)
   