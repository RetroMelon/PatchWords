import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'patchwords_project.settings')

import django
django.setup()

from django.contrib.auth.models import User as DjangoUser
from patchwords.models import *
import datetime, random


def populate():
    populate_user()
    populate_category()
    populate_story()
    populate_paragraph()
    populate_like()
    populate_favourite()


# the population functions for each part of the database
def populate_user():
    add_user("johnnyboy95", "jstarrrr@gmail.com", "password123", "I'm a kool dood.", date_of_birth=datetime.date(1995, 9, 24))
    add_user("taylors_cat", "cat@tswizzle.com", "whiskas", "I'm a kool kitty.", date_of_birth=datetime.date(2008, 1, 1))
    add_user("guiseppe", "joe@iwishiwereitalian.com", "pizza9001", "Seriously though, if you are out with your girlfriend's parents for dinner, don't order a hawaiian pizza - she will slag you forever.")
    add_user("test", "test@gmail.com", "test", "Test account :D.")


def populate_category():
    add_category("Random")
    add_category("Horror")
    add_category("Comedy")
    add_category("Twilight Fan-fic")
    add_category("T-swizzle Love-Letters")
    add_category("Sci-Fi")
    add_category("Lolz")
    add_category("Poems")
    add_category("Song Lyrics")


def trim_newline(s):
    if s[-1] == "\n":
        s = s[:-1]
    return s


def populate_story():
    # getting all of the users in the database
    users = User.objects.all()

    # getting all of the categories in the database
    categories = Category.objects.all()

    titles_file = open("titles.txt", "r")
    titles = [trim_newline(l) for l in titles_file]
    titles_file.close()

    for t in titles:
        add_story(t, random.choice(users), random.choice(categories))


def populate_paragraph():
    # a bunch of random sentences
    sentences_file = open("sentences.txt", "r")
    sentences = [trim_newline(l) for l in sentences_file]
    sentences_file.close()

    # getting all of the users in the database
    users = User.objects.all()

    # getting all of the stories in the database
    stories = Story.objects.all()

    # adding some paragraphs to each story
    for s in stories:
        # storing each paragraph in the story so we can later add to it
        paragraphs = []

        # setting up the first paragraph.
        para = add_paragraph(random.choice(sentences), s, None, s.author)
        paragraphs.append(para)

        for i in range(2):
            # creating a paragraph with random sentence, parent, user
            para = add_paragraph(random.choice(sentences), s, random.choice(paragraphs), random.choice(users))

            # adding the paragraph to the paragraphs list so that we can potentially use it as a parent
            paragraphs.append(para)


def populate_like():
    # getting all of the users in the database
    users = User.objects.all()

    # getting all of the paragraphs in the database
    paras = Paragraph.objects.all()

    for i in range(8):
        add_like(random.choice(users), random.choice(paras))


def populate_favourite():
    # getting all of the users in the database
    users = User.objects.all()

    # getting all of the stories in the database
    stories = Story.objects.all()

    for i in range(6):
        add_favourite(random.choice(users), random.choice(stories))


# the functions used to add stuff to the database
def add_user(username, email, password, bio="", date_of_birth=None, picture="profile_images/blank-user.jpg"):
    # creating the django user
    django_user = DjangoUser.objects.get_or_create(username=username, email=email)[0]
    django_user.set_password(password)
    django_user.save()

    print django_user

    # creating our kind of user
    user = UserProfile.objects.get_or_create(user=django_user, bio=bio, date_of_birth=date_of_birth, picture=picture)[0]
    print "CREATED USER: ", user
    return user


def add_category(title):
    cat = Category.objects.get_or_create(title=title)[0]
    print "CREATED CATEGORY: ", cat
    return cat


def add_story(title, author, category):
    story = Story.objects.get_or_create(title=title, author=author, category=category)[0]
    print "CREATED STORY: ", story
    return story


def add_paragraph(content, story, parent, author, end=False):
    para = Paragraph.objects.get_or_create(content=content, story=story, parent=parent, author=author, end=end)[0]
    print "CREATED PARA: ", para
    return para


def add_like(user, paragraph):
    like = Like.objects.get_or_create(user=user, paragraph=paragraph)[0]
    print "CREATED LIKE: ", like
    return like


def add_favourite(user, story):
    fav = Favourite.objects.get_or_create(user=user, story=story)[0]
    print "CREATED FAV: ", fav
    return fav


# Start execution here!
if __name__ == '__main__':
    print "Populating database."
    populate()
