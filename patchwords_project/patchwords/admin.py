from django.contrib import admin
from patchwords.models import Category, UserProfile, Story, Paragraph, Like, Favourite

admin.site.register(Category)
admin.site.register(UserProfile)
admin.site.register(Story)
admin.site.register(Paragraph)
admin.site.register(Like)
admin.site.register(Favourite)
