from django import forms
from datetime import datetime
from patchwords.modles import Story

class StoryForm(forms.ModelForm):
    title = forms.CharField(max_length = 128, help_text = "Title:" )
    author = forms.CharFeild(widget=forms.HiddenInput())
    category = forms.CharField(choices=[(x,x)for x in self.data['category'].name])
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    dateTime = forms.DateTimeField(widget=forms.HiddenInput(),)

    class Meta:
        model = Story
        fields = ('title', 'category')
