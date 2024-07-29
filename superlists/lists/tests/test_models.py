from django.core.exceptions import ValidationError
from django.test import TestCase
# from django.core.urlresolvers import resolve # depreated since Django 1.9
from lists.models import Item, List


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

    def test_cannot_save_empty_list(self):
        mylist = List.objects.create()
        item = Item(list=mylist, text='')
        with self.assertRaises(ValidationError):
            item.save()
            item.full_clean() # Django提供的用于运行全部验证，这个方法就会验证item的text为空，然后报错
            # 如果text = models.TextField(default=''， blank=True)，blank=True，那么允许字段为空，测试会报错

