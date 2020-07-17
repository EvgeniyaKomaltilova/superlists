from django.shortcuts import render, redirect
from .models import Item, List


def home_page(request):
    """домашняя страница"""
    return render(request, 'lists/home.html')


def view_list(request):
    """представление списка"""
    items = Item.objects.all()
    content = {'items': items}
    return render(request, 'lists/list.html', content)


def new_list(request):
    """новый список"""
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect('/lists/1')
