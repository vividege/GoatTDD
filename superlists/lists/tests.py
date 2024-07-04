from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import TestCase
# from django.core.urlresolvers import resolve # depreated since Django 1.9
from django.urls import resolve
from lists.views import home_page


# Create your tests here.
class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        '''
        The following code snipt was outdate due to Django version
        :========================================================:

        request = HttpRequest()
        response = home_page(request)
        self.assertTemplateUsed(response, 'home.html')
        expected_html = render_to_string('home.html', request=request)
        print(expected_html)
        result = response.content.decode()
        print("============")
        print(result)
        # self.assertTrue(response.content.startswith(b'<html>'))
        # self.assertIn(b'<title>To-Do lists</title>', response.content)
        # self.assertTrue(response.content.endswith(b'</html>'))
        self.assertEqual(result, expected_html)
        '''
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = home_page(request)
        self.assertIn('A new list item', response.content.decode())
        expected_html = render_to_string('home.html', {'new_item_text': 'A new list item'})
        print(expected_html)
        self.assertEqual(response.content.decode(), expected_html)
