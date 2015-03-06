from django import forms
from datetime import datetime
from patchwords.models import Paragraph


class NewParagraph(forms.ModelForm):
    content = forms.CharField(max_length=200, help_text="Write your paragraph!")
    choices = (
    (True, 'yes'),
    (False, 'no'))
    end = forms.ChoiceField(choices=choices, widget=forms.RadioSelect)

    class Meta:
        model = Paragraph
        exclude = ('story', 'parent', 'author','created_datetime')




