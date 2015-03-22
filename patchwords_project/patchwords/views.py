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
                             'gender':user_profile.gender}
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


    #stories = Story.objects.get(author = user_profile)
    #stories_map = (lambda x : (x.favorites, x), stories)
    #stories_map.sort()
    #stories_map.reverse()
    #context_dict['storiesMostRecent'] = stories_map[:5]

    #stories = Story.objects.get(author = user_profile).sortBy('-created_datetime')[:5]

    return render(request, 'profile.html', context_dict)

#will add story_name_slug but for the moment just request
def story(request, story_name_slug):
    context_dict = {}

    try:
        story = Story.objects.get(slug=story_name_slug)#Story.objects.get(slug=story_name_slug)
        context_dict['story'] = story

        root_paragraph = Paragraph.objects.get(parent=None, story=story)
        context_dict['root_paragraph'] = root_paragraph

        paragraphs = queries.getMostPopularSubtree(root_paragraph)
        context_dict['subtree'] = paragraphs #a list of lists of paragraphs
    except:
        pass #if we reach here we couldn't find the story, or root paragraph.


    return render(request, 'story.html', context_dict)

def render_most_popular_subtree(request, paragraph_id):
    context_dict = {}
    try:
        paragraph = Paragraph.objects.get(id=paragraph_id)
        subtree = queries.getMostPopularSubtree(paragraph)
        context_dict['subtree'] = subtree
    except:
        pass
    return render(request, 'story_block.html', context_dict)

def search(request,q):
    cat = request.GET.get("filter")
    if q:
       story_results = Story.objects.filter(title__icontains=q)[:5]
       user_results = User.objects.filter(username__icontains=q)[:5]
       category_results= Category.objects.filter(title__icontains=q)[:5]
    else:
        story_results = Story.objects.none()
        user_results=User.objects.none()
        category_results=Category.objects.none()
    context = dict(story_results=story_results, user_results=user_results, category_results=category_results, q=q,cat=cat)
    return render(request, "search.html", context)

       #story_results = Story.objects.filter(title__icontains=q).order_by('-favourite')[:5]

def search_top_stories(request):
    if request.method == 'GET':
        start = int(request.GET.get('start', 5))
        end = int(request.GET.get('end', 10))
        q = request.GET.get('q', "")

        try:
           stories = Story.objects.filter(title__icontains=q)
        except:
           stories= None

        context_dict = {}

        stories=stories[start:end]
        context_dict['stories'] = stories
        return render(request, 'stories_list.html', context_dict)