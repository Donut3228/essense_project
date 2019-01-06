from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'om_index.html', context)


def createItem(request):

    context = {}
    return render(request, 'om_create_item.html', context)
