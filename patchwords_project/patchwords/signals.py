from registration.signals import user_registered
from models import UserProfile
from forms import Registration

def user_created(sender, user, request, **kwargs):
    form = Registration(request.POST)
    data = UserProfile(user=user)
    data.picture = form.data["picture"]
    data.bio = form.data["bio"]
    data.date_of_birth = form.data["date_of_birth"]
    data.gender = form.data["gender"]
    data.save()

user_registered.connect(user_created)