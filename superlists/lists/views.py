from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from lists.forms import ItemForm
# Create your views here.
from lists.models import Item
from lists.models import List


def home_page(request):
    return render(request, 'home.html', {'form': ItemForm()})


def view_list(request, list_id):
    mylist = List.objects.get(id=list_id)
    error = None
    if request.method == 'POST':
        try:
            item = Item(text=request.POST['text'], list=mylist)
            item.full_clean()
            item.save()
            return redirect(mylist)
        except ValidationError:
            error = 'You can\'t have an empty list item'
    return render(request, 'list.html', {'list': mylist, 'error': error})


def new_list(request):
    mylist = List.objects.create()
    item = Item.objects.create(text=request.POST['text'], list=mylist)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        mylist.delete()
        error = 'You can\'t have an empty list item'
        return render(request, 'home.html', {"error": error})
    return redirect(mylist)
