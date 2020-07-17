from django.shortcuts import render, redirect
from .models import Item


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
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/lists/1')
