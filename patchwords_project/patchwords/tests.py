from django.test import TestCase
from models import *
import datetime
from django.core.urlresolvers import reverse


def add_user(username):
    test_user = User.objects.get_or_create(username=username)[0]
    test_user.save()
    return test_user

def add_story(title,author,category):
    story = Story.objects.get_or_create(title=title,author=author,category=category)[0]
    return story

def add_paragraph(story,author):
    paragraph = Paragraph.objects.get_or_create(story=story,author=author)[0]
    return paragraph

def add_category(title):
    category = Category.objects.get_or_create(title=title)[0]
    return category

def add_like(user,paragraph):
    Like.objects.get_or_create(user=user,paragraph=paragraph)[0]

def add_favourite(user,story):
    Favourite.objects.get_or_create(user=user,story=story)[0]

def add_user_profile(user, bio, date_of_birth,gender):
    user.UserProfile = UserProfile.objects.get_or_create(user=user,bio=bio,date_of_birth=date_of_birth,gender=gender)[0]
    return user


class ModelTests(TestCase):
    def test_users_can_have_story(self):
        user = add_user("test_user")
        cat = add_category("test_cat")
        story = add_story("test_story",user,cat)
        self.assertEqual(story.author,user)


    def test_stories_can_be_added_to_category(self):
        user = add_user("test_user")
        cat = add_category("test_cat")
        story = add_story("test_story",user,cat)
        self.assertEqual(story.category,cat)


    def test_paragraphs_can_be_added_to_stories(self):
        user = add_user("test_user")
        cat = add_category("test_cat")
        story = add_story("test_story",user,cat)
        paragraph = add_paragraph(story,user)
        self.assertEqual(story, paragraph.story)


    def test_paragraphs_can_be_liked(self):
        user = add_user("test_user")
        cat = add_category("test_cat")
        story = add_story("test_story",user,cat)
        paragraph = add_paragraph(story,user)
        self.assertEqual(0,paragraph.likes)
        add_like(user,paragraph)
        self.assertEqual(1,paragraph.likes)


    def test_stories_can_be_favourites(self):
        user = add_user("test_user")
        cat = add_category("test_cat")
        story = add_story("test_story",user,cat)
        self.assertEqual(0,story.favourites)
        add_favourite(user,story)
        self.assertEqual(1,story.favourites)


    def test_gender_assignment(self):
        user = add_user("test_user")
        user = add_user_profile(user,'test bio',datetime.date(1995, 9, 24),'Male')
        self.assertEqual(user.UserProfile.gender, 'Male')


    def test_female_gender_assignment(self):
        user = add_user("test_user")
        user = add_user_profile(user,'test bio',datetime.date(1995, 9, 24),'Female')
        self.assertEqual(user.UserProfile.gender, 'Female')


    def test_adding_bio(self):
        user = add_user("test_user")
        user = add_user_profile(user,'test bio',datetime.date(1995, 9, 24),'Male')
        self.assertEqual(user.UserProfile.bio, 'test bio')


    def test_date_of_birth_assignment(self):
        user = add_user("test_user")
        user = add_user_profile(user,'test bio',datetime.date(1995, 9, 24),'Male')
        self.assertEqual(user.UserProfile.date_of_birth, datetime.date(1995, 9, 24))


    def test_unique_category_slug(self):
        test_cat1 = add_category("test_1")
        test_cat2 = add_category("test_2")
        self.assertNotEqual(test_cat1.slug,test_cat2.slug)


    def test_age_assignment(self):
        user = add_user("test_user")
        user = add_user_profile(user,'test bio', datetime.date(1995, 9, 24), 'Male')
        self.assertEqual(user.UserProfile.age, 19)


    def test_slug(self):
        author = User(username='username', password = 'password')
        author.save()
        category = Category(title = 'testtest')
        category.save()
        story = Story(title = 'this is a test story', author = author, category = category)
        story.save()
        self.assertEqual(story.slug, 'this-is-a-test-story')


class HomeViewTest(TestCase):
    def test_home_with_no_stories(self):
        cat = add_category("test cat")
        response = self.client.get(reverse('home'))
        num_stories =len(response.context['stories'])
        self.assertEqual(num_stories , 0)

    def test_home_story(self):
        user = add_user('username')
        cat = add_category('test')
        story = add_story('test', user, cat)
        response = self.client.get(reverse('home'))
        self.assertContains(response, story)

class CategoryViewTest(TestCase):

    def test_story_in_cat_page(self):
        user = add_user('username')
        add_category('storyisin')
        add_category('storyisntin')
        cat = Category.objects.get(title = 'storyisin')
        story = add_story('test', user, cat)
        response = self.client.get('/patchwords/category/storyisin/')
        self.assertContains(response, story)

    def test_story_not_in_cat_page(self):
        user = add_user('username')
        add_category('storyisin')
        add_category('storyisntin')
        cat = Category.objects.get(title = 'storyisin')
        story = add_story('test', user, cat)
        response = self.client.get('/patchwords/category/storyisntin/')
        num_stories = len(response.context['stories'])
        self.assertEqual(num_stories , 0)
        
class AllCategoriesTest(TestCase):
    def test_allcategories_empty(self):
        response = self.client.get(reverse('all_categories'))
        num_cat = len(response.context['categories'])
        self.assertEqual(num_cat , 0)
        cat = add_category('test')
        add_category('test2')
        response = self.client.get(reverse('all_categories'))
        self.assertContains(response, cat)
        num_cat = len(response.context['categories'])
        self.assertEqual(num_cat , 2)

class StoriesTest(TestCase):
    def test_story(self):
        user = add_user('username')
        cat = add_category('storyisin')
        story = add_story('test', user, cat)
        response = self.client.get('/patchwords/story/test/')
        self.assertContains(response, story)
        
class SearchTest(TestCase):
    def test_search_test(self):
        user = add_user('Bob')
        cat = add_category('Job')
        story = add_story('Job', user, cat)
        user2 = add_user('Kerry')
        response = self.client.get('/patchwords/search/?parameter=Job&filter=All')
        self.assertContains(response, story)
        self.assertNotContains(response, user2)
