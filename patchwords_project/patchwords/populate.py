import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from django.contrib.auth.models import User as DjangoUser
from patchwords.models import *


def populate():
    populate_user()
    populate_category()
    populate_story()
    populate_paragraph()
    populate_like()
    populate_favourite()


#the population functions for each part of the database
def populate_user():
    pass

def populate_category():
    pass

def populate_story():
    pass

def populate_paragraph():
    pass

def populate_like():
    pass

def populate_favourite():
    pass


#the functions used to add stuff to the database
def add_user(username, password, email, first_name, last_name, picture = None):
    pass

def add_category(title):
    pass

def add_story(title, author, category):
    pass

def add_paragraph(story, parent, views, author, end = False):
    pass


# Start execution here!
if __name__ == '__main__':
    print "Populating database."
    populate()
