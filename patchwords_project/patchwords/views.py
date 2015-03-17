from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from models import *
import sys, queries


from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
    context_dict = {}

    #getting the most popular categories
    categories = queries.getTopCategories()
    context_dict['categories'] = categories

    #getting the most popular stories
    stories = queries.getTopStories(start=0, end=2)
    context_dict['stories'] = stories

    return render(request, 'home.html', context_dict)


def get_top_stories(request):
    if request.method == 'GET':
        start = int(request.GET.get('start', 0))
        end = int(request.GET.get('end', 2))
        category = request.GET.get('category', "")

        try:
            category = Category.objects.get(title=category)
        except:
            category = None

        context_dict = {}

        stories = queries.getTopStories(start, end, category)
        context_dict['stories'] = stories

        return render(request, 'stories_list.html', context_dict)



def category(request, category_name_slug):
    context_dict= {}
    category = Category.objects.get(slug=category_name_slug)
    context_dict['category'] = category
    context_dict['category_name_slug'] = category_name_slug

    #stories = Story.objects.filter(category=category)
    stories = queries.getTopStories(start=0, end=2)
    context_dict['stories'] = stories_map[:20]

    return render(request, 'category.html', context_dict)

def all_categories(request):
    categories = Category.objects.all().sortBy("title")
    categories_map = (lambda x: (x.title, x.slug), categories)
    return render(request, 'all_categories.html',{'categories': categories_map})

def user(request, username):
    context_dict = {}
    user = UserProfile.objects.get(name = username)
    context_dict['name'] = user.user
    context_dict['bio'] = user.bio
    context_dict['age'] = user.age
    context_dict['picture'] = user.picture

    stories = Story.objects.get(user = author)
    stories_map = (lambda x : (x.favorites, x), stories)
    stories_map.sort()
    stories_map.reverse()
    context_dict['storiesMostRecent'] = stories_map[:5]

    stories = stories = Story.objects.get(user = author).sortBy('-created_datetime')[:5]

    return(request, 'category.html', context_dict)

#will add story_name_slug but for the moment just request
def story(request, story_name_slug):
    story = Story.objects.get(slug=story_name_slug)
    return render(request, 'story.html', {})
    #need to add the most contributed paragraphs and highest liked paragraphs

    return render(request, 'user.html', context_dict)

