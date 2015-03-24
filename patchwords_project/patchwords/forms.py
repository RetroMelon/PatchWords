from django import forms
from registration.forms import RegistrationForm
from django.contrib.auth.models import User
from models import UserProfile
from models import *

class Registration(RegistrationForm):
    picture = forms.ImageField(required=False)
    bio = forms.CharField(widget=forms.Textarea(),required=False)
    date_of_birth = forms.DateField(input_formats=['%d/%m/%Y'],required=False)
    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),)
    gender = forms.ChoiceField(widget=forms.RadioSelect,
                               choices=GENDER_CHOICES,required=False)

class UserForm(forms.ModelForm):
    username = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('username','email',)

class UserProfileForm(forms.ModelForm):
    GENDER_CHOICES = (
        ("Male", "Male"),
        ("Female", "Female"),)
    gender = forms.ChoiceField(widget=forms.RadioSelect,
                               choices=GENDER_CHOICES,required=False)

    class Meta:
        model = UserProfile
        fields = ('picture','bio','gender')


class ParagraphForm(forms.ModelForm):
    content = forms.CharField(max_length=200, help_text="Write your paragraph!")
    choices = (
    (True, 'yes'),
    (False, 'no'))
    end = forms.ChoiceField(choices=choices, widget=forms.RadioSelect)

    class Meta:
        model = Paragraph
        exclude = ('story', 'parent', 'author','created_datetime')

class StoryForm(forms.ModelForm):
    title = forms.CharField(max_length=100, help_text='Title', required = True)
    #category = forms.ModelChoiceField(queryset=Category.objects.all().order_by('title'), help_text = "Category", required = True)
    cat = forms.CharField(required = True)
    text = forms.CharField(max_length=140, help_text="First Paragraph", required = True)
    class Meta:
        model = Story
        exclude = ('created_datetime', 'author', 'slug', 'category')

