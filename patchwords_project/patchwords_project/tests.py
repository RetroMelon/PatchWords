from django.test import TestCase
from patchwords.models import *

# pls don't remove - need to find out whether saving is needed

def add_category(name):
    test_cat = Category.objects.get_or_create(name=name)
    test_cat.save()
    return test_cat

def add_user(bio,date_of_birth,gender,):
    picture= '/media/profile_images/blank-user.jpg'
    test_user = UserProfile.objects.get_or_create(bio=bio,date_of_birth=date_of_birth,gender=gender,picture=picture)
    test_user.save()
    return test_user

def add_story(title,test_user,test_cat):
    test_story = Story.objects.get_or_create(title=title,author=test_user.username,category=test_cat)
    test_story.save()
    return test_story

class ModelTests(TestCase):
    def test_category(self):
        pass