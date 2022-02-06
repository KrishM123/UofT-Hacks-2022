from django import forms
from django.forms.widgets import MultiWidget
from WebApp.models import *

class loginForms(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput({'placeholder': 'Username'}))
    password = forms.CharField(required=True, widget=forms.TextInput({'placeholder': 'Password'}))

OPTIONS = [
    ('Student', 'Student'),
    ('Teacher', 'Teacher')
    ]
class signUpForms(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput({'placeholder': 'Enter you name'}))
    username = forms.CharField(required=True, widget=forms.TextInput({'placeholder': 'Set username'}))
    password = forms.CharField(required=True, widget=forms.TextInput({'placeholder': 'Set password'}))
    type = forms.CharField(widget=forms.Select(choices=OPTIONS))
    email = forms.EmailField(required=True, widget=forms.TextInput({'placeholder': 'Enter your email'}))

class createQuestion(forms.Form):
    question = forms.CharField(required=True, widget=forms.TextInput({'placeholder': 'Question'}))
    Option1 = forms.CharField(required=True, widget=forms.TextInput({'placeholder': 'Option 1'}))
    Option2 = forms.CharField(required=True, widget=forms.TextInput({'placeholder': 'Option 2'}))
    Option3 = forms.CharField(required=True, widget=forms.TextInput({'placeholder': 'Option 3'}))
    Option4 = forms.CharField(required=True, widget=forms.TextInput({'placeholder': 'Option 4'}))
    CHOICES = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')]
    answer = forms.CharField(label='Answer', widget=forms.RadioSelect(choices=CHOICES))
    Tag1 = forms.CharField(required=True, widget=forms.TextInput({'placeholder': 'Tag'}))
    Tag2 = forms.CharField(required=False, widget=forms.TextInput({'placeholder': 'Tag'}))
    Tag3 = forms.CharField(required=False, widget=forms.TextInput({'placeholder': 'Tag'}))
    Tag4 = forms.CharField(required=False, widget=forms.TextInput({'placeholder': 'Tag'}))
    Tag5 = forms.CharField(required=False, widget=forms.TextInput({'placeholder': 'Tag'}))
    Tag6 = forms.CharField(required=False, widget=forms.TextInput({'placeholder': 'Tag'}))
    Tag7 = forms.CharField(required=False, widget=forms.TextInput({'placeholder': 'Tag'}))
    Tag8 = forms.CharField(required=False, widget=forms.TextInput({'placeholder': 'Tag'}))
    Tag9 = forms.CharField(required=False, widget=forms.TextInput({'placeholder': 'Tag'}))
    Tag10 = forms.CharField(required=False, widget=forms.TextInput({'placeholder': 'Tag'}))