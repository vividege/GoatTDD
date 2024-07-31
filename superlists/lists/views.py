from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect

# Create your views here.
from lists.models import Item

from lists.models import List


def home_page(request):
    return render(request, 'home.html')


def view_list(request, list_id):
    mylist = List.objects.get(id=list_id)
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'], list=mylist)
        return redirect('/lists/{0}/'.format(mylist.id))
    return render(request, 'list.html', {'list': mylist})


def new_list(request):
    mylist = List.objects.create()
    item = Item.objects.create(text=request.POST['item_text'], list=mylist)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        mylist.delete()
        error = 'You can\'t have an empty list item'
        return render(request, 'home.html', {"error": error})
    return redirect(f'/lists/{mylist.id}/')
