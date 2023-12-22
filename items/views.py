from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Items

# Create your views here.

def index(request):
   item_list = Items.objects.all()
   context = { "item_list": item_list }
   return render(request,"items/index.html", context)

def detail(request,item_code):
    try:
        item = Items.objects.get(pk=item_code)
    except Items.DoesNotExist:
        raise Http404("Item does not exist")
    return render(request,"items/detail.html",{"item" : item} )
def price(request, item_code):
    return HttpResponse("Your are looking at item price of %s" %item_code)


def unit(request, item_code):
    return HttpResponse(" You are looking at unit of %s item" %item_code)
