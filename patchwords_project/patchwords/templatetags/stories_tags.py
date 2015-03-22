from django import template
from patchwords.models import *

register = template.Library()


#checks if a user has liked the paragraph
@register.filter
def liked_by(paragraph, user):
    return bool(len(Like.objects.filter(user=user, paragraph=paragraph)))


@register.filter
def favourited_by(story, user):
    return bool(len(Favourite.objects.filter(user=user, story=story)))
