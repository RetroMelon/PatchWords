from datetime import date
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images',blank=True)
    bio = models.TextField(blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    #the choices for gender
    MALE = 'Male'
    FEMALE = 'Female'
    NOT_SPECIFIED = 'Not Specified'

    GENDER_CHOICES = (
        (MALE, 'Male'), (FEMALE, 'Female'), (NOT_SPECIFIED, 'Not Specified'),
    )

    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default=NOT_SPECIFIED)

    @property
    def age(self):
        today = date.today()
        date_of_birth = self.date_of_birth
        return today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))

    def __unicode__(self):
        return self.user.username

import signals

class Category(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title



class Story(models.Model):
    created_datetime = models.DateTimeField(auto_now_add = True)

    title = models.CharField(max_length = 128, unique=True)
    author = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Story, self).save(*args, **kwargs)

    @property
    def favourites(self):
        #getting all of the favourites for this story from the database
        favourites_list = Favourite.objects.filter(story=self)
        #returning the count
        return len(favourites_list)

    @property
    def outline(self):
        root_paragraph = Paragraph.objects.get(story=self, parent=None)
        return root_paragraph.content

    def __unicode__(self):
        return self.title


class Paragraph(models.Model):
    created_datetime = models.DateTimeField(auto_now_add = True)

    content = models.CharField(max_length=200)
    story = models.ForeignKey(Story)
    parent = models.ForeignKey('self', null=True)
    author = models.ForeignKey(User)
    end = models.BooleanField(default=False)

    def __unicode__(self):
        return self.author.username + ": " + self.content[:20] + "..."

    #prints this tree with a subtree
    def _print_subtree(self, depth=0):
        #printing itself
        print "|" + "-"*depth*2 + "|" + str(self)

        #iterating over all of its children and printing them with depth+1
        for c in Paragraph.objects.filter(parent=self):
            c._print_subtree(depth=depth+1)



class Favourite(models.Model):
    user = models.ForeignKey(User)
    story = models.ForeignKey(Story)

    def __unicode__(self):
            return self.user.username + " FAVS " + self.story.title


class Like(models.Model):
    user = models.ForeignKey(User)
    paragraph = models.ForeignKey(Paragraph)

    def __unicode__(self):
        return self.user.username + " Likes \"" + self.paragraph.content[:20] + "\"..."
