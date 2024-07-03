from django.test import TestCase
# from django.core.urlresolvers import resolve # depreated since Django 1.9
from django.urls import resolve
from lists.views import home_page

# Create your tests here.
class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        print(found.func)
        self.assertEqual(found.func, home_page)