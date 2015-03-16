from django import forms
from registration.forms import RegistrationForm
from django.contrib.auth.models import User

from patchwords.models import UserProfile

class Registration(RegistrationForm):
    picture = forms.ImageField(required=False)
    bio = forms.CharField(widget=forms.Textarea(),required=False)
    date_of_birth = forms.DateField(input_formats=['%Y-%m-%d'],required=False)
    GENDER_CHOICES = (
            ("Male", "Male"),
            ("Female", "Female"),
            )
    gender = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                         choices=GENDER_CHOICES,required=False,
                                         )


class NewParagraph(forms.ModelForm):
    content = forms.CharField(max_length=200, help_text="Write your paragraph!")
    choices = (
    (True, 'yes'),
    (False, 'no'))
    end = forms.ChoiceField(choices=choices, widget=forms.RadioSelect)

    class Meta:
        #model = Paragraph
        exclude = ('story', 'parent', 'author','created_datetime')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email','password')



class UserLogin(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields =('username', 'password')
