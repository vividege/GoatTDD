from django.shortcuts import render, redirect
from lists.forms import ItemForm
# Create your views here.
from lists.models import Item
from lists.models import List


def home_page(request):
    return render(request, 'home.html', {'form': ItemForm()})


def view_list(request, list_id):
    mylist = List.objects.get(id=list_id)
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(data=request.POST)
        if form.is_valid():
            form.save(for_list=mylist)
            return redirect(mylist)
    return render(request, 'list.html', {'list': mylist, 'form': form})


def new_list(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
        mylist = List.objects.create()
        form.save(for_list = mylist)
        return redirect(mylist)
    else:
        return render(request, 'home.html', {"form": form})
