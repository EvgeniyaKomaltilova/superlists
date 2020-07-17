from django.db import models


class Item(models.Model):
    """элемент списка"""
    text = models.TextField(default='')
    list = models.ForeignKey('List', default=None, on_delete=models.CASCADE)


class List(models.Model):
    """список"""
    name = models.CharField(max_length=255)
