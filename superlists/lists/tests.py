from django.test import TestCase
# from django.core.urlresolvers import resolve # depreated since Django 1.9
from django.urls import resolve
from lists.models import Item,List
from lists.views import home_page


class NewListTest(TestCase):
    def test_saving_a_POST_request(self):
        self.client.post(
            '/lists/new',
            data={'item_text': 'A new list item'}
        )
        self.assertEqual(Item.objects.count(), 1)  # check a newly added item is in DB
        new_item = Item.objects.first()  # == objects.all()[0]
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        response = self.client.post(
            '/lists/new',
            data={'item_text': 'A new list item'}
        )

        # after post, the page needs to be redirected
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/lists/the-only-list-in-the-world/')
        self.assertRedirects(response, '/lists/the-only-list-in-the-world/')


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


class ListAndItemModelTest(TestCase):
    def test_saving_and_retrieving_items(self):
        mylist = List()
        mylist.save()

        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.list = mylist
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.list = mylist
        second_item.save()

        saved_list = List.objects.get()
        # saved_list: NoneType
        # mylist: <List: List object (None)>
        self.assertEqual(saved_list, mylist)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(first_saved_item.list, mylist)
        self.assertEqual(second_saved_item.text, 'Item the second')
        self.assertEqual(second_saved_item.list, mylist)


class ListViewTest(TestCase):
    # check list view use another html template not "home.html"
    def test_uses_list_template(self):
        response = self.client.get('/lists/the-only-list-in-the-world/')
        self.assertTemplateUsed(response, 'list.html')

    def test_displays_all_items(self):
        mylist = List.objects.create()
        Item.objects.create(text='itemey 1', list=mylist)
        Item.objects.create(text='itemey 2', list=mylist)

        response = self.client.get('/lists/the-only-list-in-the-world/')

        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')
