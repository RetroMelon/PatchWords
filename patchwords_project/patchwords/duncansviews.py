from django.shortcuts import render
from django.contrib.auth.models import User
from patchwords.models import UserProfile
from django.contrib.auth.decorators import login_required

from patchwords.duncansforms import NewParagraph
def new_paragraph(request):

    story = currentUrl
    if request.method == 'POST':
        newparagraph = NewParagraph(data=request.post)
        username = request.POST.get('username')



    return(request, 'patchwords/')
