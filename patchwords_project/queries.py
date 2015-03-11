# The queries.py file contains a bunch of relatively complex database
# queries that probably shouldn't take place inside the views.
from patchwords.models import Category, Story

#gets a list of
def getTopStories(start=0, end=20, category=None):
    #getting the stories and zipping them with their favourites
    if not category:
        stories = Story.objects.all()
    else:
        stories = Story.objects.filter(category=category)

    stories_ordered = zip(map(lambda x : x.favourites, stories), stories)

    #sorting the stories
    stories_ordered.sort()
    stories_ordered.reverse()

    #unzipping the stories
    stories_ordered = zip(*(stories_ordered))[1]

    return stories_ordered[start:end]

def getTopCategories(quantity=20):
    #getting the categories and mapping them with their favourites.
    cats = Category.objects.all()
    cats_with_story_count = map(lambda x: (x.total_stories, x), cats)

    cats_with_story_count.sort()
    cats_with_story_count.reverse()

    #unzipping the categories
    cats_with_story_count = zip(*(cats_with_story_count))[1]

    #returning the top 20
    return cats_with_story_count[:quantity]
