from django import forms
from .models import Task,User
#from django.contrib.auth.models import User
from django.contrib.auth.forms import (UserCreationForm,
                                       UserChangeForm)
class AddTaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=["head","desc","user"]
        widgets={'user':forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(AddTaskForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        task = super(AddTaskForm, self).save(commit=False)
        if self.user:
            task.user = self.user
        if commit:
            task.save()
        return task

from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'gender', 'occupation', 'phone_number']# 'password1', 'password2']
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'first_name', 'last_name', 'gender', 'occupation', 'phone_number']#, 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(attrs={'autofocus': True}))

    class Meta:
        model = User
        fields = ('email', 'password')

"""
class SignupForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'username', 'first_name', 'last_name', 'gender', 'occupation', 'phone_number')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user"""
"""
class CustomUserChangeForm(UserChangeForm):
 class Meta:
     model = User
     fields = UserChangeForm.Meta.fields
class SignupForm(UserCreationForm):
    
   class Meta:
        model=User
        fields=("email","username","first_name","last_name","gender","occupation","phone_number")
class LoginForm(forms.Form):

    email=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)"""