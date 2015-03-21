# The queries.py file contains a bunch of relatively complex database
# queries that probably shouldn't take place inside the views.
from patchwords.models import Category, Story, Paragraph

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

def _sortParagraphs(paragraphs):
    if not paragraphs:
        return []
    #zipping paragraphs with likes
    zipped = map(lambda x: (x.likes, x), paragraphs)
    zipped.sort()
    zipped.reverse()

    unzipped = zip(*zipped)[1]
    return unzipped

#a wrapper around getMostPopularSubtree
def getMostPopularSubtree(paragraph):
    return _getMostPopularSubtree([paragraph,])

#given a paragraph lis, this returns a list of lists of paragraphs.
#it assumes that the first paragraph in the list is the most popular
def _getMostPopularSubtree(paragraphs):
    #getting the most popular paragraph's children
    child_paragraphs = Paragraph.objects.filter(parent=paragraphs[0])


    #sorting all of the children
    child_paragraphs = _sortParagraphs(child_paragraphs)
    #print "child paragraphs: \n\n", child_paragraphs

    #adding the children to the list of things to return
    return_list = [child_paragraphs,]

    #if the children list is not empty, then we extend te list with the most popular subtree
    if child_paragraphs:
        return_list.extend(_getMostPopularSubtree(child_paragraphs))

    return return_list
