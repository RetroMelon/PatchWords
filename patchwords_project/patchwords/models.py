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


