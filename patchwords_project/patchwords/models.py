from datetime import date
from django.db import models
from django.contrib.auth.models import User
#from django.template.defaultfilters import slugify

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images',blank=True)
    bio = models.TextField(blank=True)
    date_of_birth = models.DateField(blank=True)

    MALE = 'Male'
    FEMALE = 'Female'
    NOT_SPECIFIED = 'Not Specified'

    GENDER_CHOICES = (
        (MALE, 'Male'), (FEMALE, 'Female'), (NOT_SPECIFIED, 'Not Specified'),
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default=NOT_SPEFICIED)

    def calculate_age(self):
        today = date.today()
        date_of_birth = self.date_of_birth
        return today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))

    def __unicode__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.title


class Paragraph(models.Model):
    story = models.ForeignKey(Story)
    parent = models.ForeignKey('self')
    views = models.IntegerField(default=0)
    author = models.ForeignKey(User)
    created_datetime = models.DateTimeField(auto_now_add = True)
    end = models.BooleanField(default=False)

    def __unicode__(self):
        return self.author.username


class Favourite(models.Model):
    user = models.ForeignKey(UserProfile)
    story = models.ForeignKey(Story)

    def __unicode__(self):
            return self.user.username


class Story(models.Model):
    title = models.CharField(max_length = 128, unique=True)
    author = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    created_datetime = models.DateTimeField(auto_now_add = True)
    slug = models.SlugField()

    def __unicode__(self):
        return self.title


class Like(models.Model):
    user = models.ForeignKey(User)
    paragraph = models.ForeignKey(Paragraph)

    def __unicode__(self):
        return self.user.username
