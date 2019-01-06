from django.shortcuts import render, get_object_or_404
from essence_web_app.models import Item, Brand, Category, SubCategory, Picture
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from essence_web_app.serializers import ItemSerializer, BrandSerializer, CategorySerializer, SubCategorySerializer
from rest_framework import viewsets, generics
import random


def index(request):
    context = {}
    return render(request, 'index.html', context)


def shop(request):

    item_list = Item.objects.all()
    # переводим цену всех товаров в доллары и добавляем 2 ноля после запятой
    for item in item_list:
        item.price = format(item.price / 100, '.2f')

    picture_list = []
    for item in item_list:
        picture_list.append(Picture.objects.filter(item_id=item.id).order_by('id')[:2])
    picture_links = []
    for pic in picture_list:
        for each in pic:
            picture_links.append('img/product-img/' + each.pic_name)
    picture_links.reverse()

    context = {'items': item_list, 'categories': Category.objects.all().order_by('name'),
               'subcategories':SubCategory.objects.all().order_by('category__name'),
               'pictures': picture_links, 'items_amount': item_list.__len__()}

    return render(request, 'shop.html', context)


# def shop_filter(request, pk):
#     item_list = Item.objects.filter(subcategory__id=pk)
#
#     # переводим цену всех товаров в доллары и добавляем 2 ноля после запятой
#     for item in item_list:
#         item.price = format(item.price / 100, '.2f')
#
#     picture_list = []
#     for item in item_list:
#         picture_list.append(Picture.objects.filter(item_id=item.id).order_by('id')[:2])
#     picture_links = []
#     for pic in picture_list:
#         for each in pic:
#             picture_links.append('img/product-img/' + each.pic_name)
#     picture_links.reverse()
#
#     context = {'items': item_list, 'categories': Category.objects.all().order_by('name'),
#                'subcategories': SubCategory.objects.all().order_by('category__name'),
#                'pictures': picture_links, 'items_amount': item_list.__len__()}
#
#     return render(request, 'shop.html', context)


def checkout(request):
    context = {}
    return render(request, 'checkout.html', context)


def items(request):
    item_list = Item.objects.all()
    coin = random.randint(1, 15)
    # переводим цену всех товаров в доллары и добавляем 2 ноля после запятой
    for item in item_list:
        item.price = format(item.price / 100, '.2f')
    context = {'items': item_list, 'categories': Category.objects.all(),
               'subcategories': SubCategory.objects.all(),
               'coin': coin}
    return render(request, 'items.html', context)


def item_detail(request, pk):

    item = get_object_or_404(Item, pk=pk)

    # получаем три картинки товара
    picture_list = Picture.objects.filter(item_id=pk).order_by('pic_name')[:3]

    # создаем ссылку для каждой картинки
    picture_links = []
    for picture in picture_list:
        picture_links.append('img/product-img/' + picture.pic_name)

    # переводим цену из центов в доллары и добавляем 2 ноля после запятой
    item.price = format(item.price / 100, '.2f')

    context = {'item': item, 'pictures': picture_links}
    return render(request, 'item.html', context)
