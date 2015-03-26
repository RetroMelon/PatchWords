from registration.signals import user_registered
from models import UserProfile
from forms import Registration
import datetime
from datetime import date

def user_created(sender, user, request, **kwargs):
    form = Registration(request.POST)
    data = UserProfile(user=user)
    try:
        data.picture = request.FILES['picture']
    except:
        data.picture = '/media/profile_images/blank-user.jpg'
    try:
        data.bio = form.data["bio"]
    except:
        pass
    try:
        string_date = form.data["date_of_birth"]
        string_date_formatted = string_date[6:]+string_date[3:5]+string_date[:2]
        d = datetime.datetime.strptime(string_date_formatted, "%Y%m%d").date()
        data.date_of_birth = d
    except:
        data.date_of_birth = None
    try:
        data.gender = form.data["gender"]
    except:
        data.gender = None
    data.save()

user_registered.connect(user_created)
