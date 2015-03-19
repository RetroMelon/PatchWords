from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from models import *
import sys, queries
from forms import *


# Create your views here.
def home(request):
    context_dict = {}

    #getting the most popular categories
    categories = queries.getTopCategories()
    context_dict['categories'] = categories

    #getting the most popular stories
    stories = queries.getTopStories(start=0)
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

    try:
        category = Category.objects.get(slug=category_name_slug)
        context_dict['category'] = category
        context_dict['category_name_slug'] = category_name_slug
        stories = queries.getTopStories()
        context_dict['stories'] = stories
    except:
        pass

    return render(request, 'category.html', context_dict)

def all_categories(request):
    categories = Category.objects.all().order_by("title")
    return render(request, 'all_categories.html',{'categories': categories})

def edit_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        username = request.user.username
        user_form = UserForm(request.POST, instance=user_profile.user)
        user_profile_form = UserProfileForm(request.POST, instance=user_profile)
        if user_form.is_valid():
            profile_to_edit = user_form.save(commit=False)
            profile_to_edit.save()
        if user_profile_form.is_valid():
            profile_to_edit = user_profile_form.save(commit=False)
            try:
                profile_to_edit.picture = request.FILES['picture']
            except:
                pass
            profile_to_edit.save()
            return profile(request,username,user_profile=user_profile)
    else:
        user_data = {'username': user_profile.user.username,'email':user_profile.user.email}
        user_profile_data = {'picture': user_profile.picture, 'bio':user_profile.bio,
                             'gender':'Male'}
        context_dict = {}
        context_dict['user_form'] = UserForm(initial=user_data)
        context_dict['user_profile_form'] = UserProfileForm(initial=user_profile_data)
        return render(request, 'edit_profile.html', context_dict)

def profile(request, username, user_profile=None):
    if user_profile:
        flag = True
        user_profile = user_profile
    else:
        flag = False
        user = User.objects.get(username=username)
        user_profile = UserProfile.objects.get(user=user)
        actual_user = User.objects.get(username=request.user.username)
    context_dict = {}
    context_dict['user'] = user_profile.user
    context_dict['user_profile'] = user_profile
    if flag:
        context_dict['flag'] = True
    else:
        context_dict['flag'] = (actual_user.username == username)


    #stories = Story.objects.get(user = author)
    #stories_map = (lambda x : (x.favorites, x), stories)
    #stories_map.sort()
    #stories_map.reverse()
    #context_dict['storiesMostRecent'] = stories_map[:5]

    #stories = Story.objects.get(user = author).sortBy('-created_datetime')[:5]

    return render(request, 'profile.html', context_dict)

#will add story_name_slug but for the moment just request
def story(request, story_name_slug):
    story = Story.objects.get(slug=story_name_slug)
    return render(request, 'story.html', {})
    #need to add the most contributed paragraphs and highest liked paragraphs

    return render(request, 'user.html', context_dict)

def search(request):
    q = request.GET.get("q")
    if q:
       # you may want to use `__istartswith' instead
       story_results = Story.objects.filter(name__icontains=q)
       user_results = User.objects.filter(name_icontainers=q)
    else:
       # you may want to return Customer.objects.none() instead
       results = Story.objects.none()
    context = dict(results=results, q=q)
    return render(request, "search.html", context)
