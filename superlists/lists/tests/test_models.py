from django.core.exceptions import ValidationError
from django.test import TestCase
# from django.core.urlresolvers import resolve # depreated since Django 1.9
from lists.models import Item, List


class ListAndItemModelTest(TestCase):
    def test_default_text(self):
        item = Item()
        self.assertEqual(item.text, '')

    def test_item_is_related_to_list(self):
        mylist = List.objects.create()
        item = Item()
        item.list = mylist
        item.save()
        self.assertIn(item, mylist.item_set.all())

    def test_cannot_save_empty_list(self):
        mylist = List.objects.create()
        item = Item(list=mylist, text='')
        with self.assertRaises(ValidationError):
            item.save()
            item.full_clean() # Django提供的用于运行全部验证，这个方法就会验证item的text为空，然后报错
            # 如果text = models.TextField(default=''， blank=True)，blank=True，那么允许字段为空，测试会报错

    def test_get_absolute_url(self):
        mylist = List.objects.create()
        self.assertEqual(mylist.get_absolute_url(), '/lists/{0}/'.format(mylist.id))

    def test_duplicate_items_are_invalid(self):
        mylist = List.objects.create()
        Item.objects.create(list=mylist, text='bla')
        with self.assertRaises(ValidationError):
            item = Item(list=mylist, text='bla')
            item.full_clean()

    def test_CAN_save_same_item_to_different_lists(self):
        list1 = List.objects.create()
        list2 = List.objects.create()
        Item.objects.create(list=list1, text='bla')
        item = Item(list=list2, text='bla')
        item.full_clean() #不该抛出异常

    def test_list_ordering(self):

        list1 = List.objects.create()
        item1 = Item.objects.create(list=list1, text='i1')
        item2 = Item.objects.create(list=list1, text='item 2')
        item3 = Item.objects.create(list=list1, text='3')
        self.assertEqual(
            list(Item.objects.all()),
            [item1, item2, item3]
        )

    def test_string_representation(self):
        item = Item(text='some text')
        self.assertEqual(str(item), 'some text')