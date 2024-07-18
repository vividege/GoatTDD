from django.shortcuts import render, redirect

# Create your views here.
from lists.models import Item

from lists.models import List


def home_page(request):
    return render(request, 'home.html')


def view_list(request, list_id):
    mylist = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list': mylist})


def new_list(request):
    mylist = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=mylist)
    return redirect(f'/lists/{mylist.id}/')

def add_item(request, list_id):
    mylist = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=mylist)
    return redirect(f'/lists/{mylist.id}/')
