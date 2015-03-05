from django import forms
from registration.forms import RegistrationForm

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


