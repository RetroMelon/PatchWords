from django.shortcuts import render
from django.http import HttpResponse
from patchwords import forms
from patchwords.models import *
import sys

# Create your views here.
def home(request):
    return render(request, 'home.html', {})

def test_stories_chunk(request):
    context_dict = {}
    #sorts the data, the stories entry into context_dict is a list of tuples
    #with the story name and the number of favorites
    stories = Story.objects.all()
    stories_map = map(lambda x : (x.favourites, x), stories)
    stories_map.sort()
    stories_map.reverse()
    context_dict['stories'] = stories_map[:20]

    return render(request, 'test_stories_chunk.html', context_dict)



# Allows you to test a form by using ?form=<form_name>
def test_form(request):
    #turns the url parameter in to a class
    def str2Class(str):
        x = getattr(forms, str)
        return x
    #then the request must be a GET
    #getting the form name we want to test from the request
    form_name = request.GET.get("form", "")
    form_class = str2Class(form_name)

    if request.method == "POST":
        return_string = str(request.POST)
        print return_string
        return HttpResponse("Your POST looked like this:  <br><br>" + return_string)
    else:
        return render(request, 'test_form.html', {'form': form_class(), 'form_name': form_name})

def category(request, category_name_slug):
    category = Category.objects.get(slug=category_name_slug)
    context_dict['category'] = category
    context_dict['category_name_slug'] = category_name_slug

    #sorts the data, the stories entry into context_dict is a list of tuples
    #with the story name and the number of favorites
    stories = Story.objects.filter(category=category)
    stories_map = (lambda x : (x.favorites, x), stories)
    stories_map.sort()
    stories_map.reverse()
    context_dict['stories'] = stories_map[:20]

    return(request, 'category.html', context_dict)

def allCategories(request):
    categories = Category.objects.all().sortBy("title")
    return(request, 'allCategories.html',{'categories': categories})
