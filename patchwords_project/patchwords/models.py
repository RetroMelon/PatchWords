from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images',blank=true)

    def __unicode__(self):
        return self.user.username

class Category(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(unique=True)

    def __unicode__(self):
        return self.title

class Paragraph(models.Model):
    story = models.ForeignKey(Story)
    parent = ForeignKey(Paragrah)
    views = models.IntegerField(default=0)
    author = models.ForeignKey(Author)
    created_datetime = models.DateTimeField(auto_now_add = True)
    end = BooleanField(default=false)

class Favourite(models.Model):
    user = ForeignKey(user.username)
    story = models.ForeignKey(Story)

class Story(models.Models):
    title = models.CharField(max_length = 128, unique=True)
    author = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    dateTime = models.DateTimeFeidl(auto_now_add = True)
    slug = model.SlugField()

class Like(models.Models):
    user = models.ForeignKey(User)
    paragraph = models.ForeignKey(Paragraph)
