from django.shortcuts import render

# Create your views here.
from urllib.parse import quote

from django.contrib import messages
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import PermissionDenied
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import ItemForm
from .models import Item
# Create your views here.

#CRUD for blogs
def item_create(request):
    form = ItemForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.created_by = request.user
        instance.save()
        messages.success(request,"Successfully created")
        return redirect('/')
    elif form.errors:
        messages.error(request,"Nope, not created")
    context = {
        "form": form,
        }
    return render(request,'item_form.html', context)


def item_list(request):
    today = timezone.now().date()
    queryset1 = Item.objects.filter(pending=True, private=False)
    if request.user:
        queryset2 = Item.objects.filter(pending=True, private=True, created_by=request.user)
        queryset = queryset1 | queryset2
    else:
        queryset = queryset1
    context = {
        "title":"Shopping List",
        "object_list": queryset,
        "today": today,
    }
    return render(request,'item_list.html',context)

def item_detail(request,id):
    item = get_object_or_404(Item,id=id)
    obj_id = item.id
    context = {
        "title": item.item_name,
        "item": item,
    }
    return render(request,'item_detail.html',context)

def buy_item(request, id):
    item = get_object_or_404(Item,id=id)
    item.finalized_by = request.user
    item.finalized = timezone.now()
    item.pending = False
    item.save()
    return redirect('/')

def reactivate_item(request, id):
    item = get_object_or_404(Item,id=id)
    item.updated = timezone.now()
    item.updated_by = request.user
    item.finalized = None
    item.finalized_by = None
    item.pending = True
    print("okay")
    item.save()
    return redirect('/')

def item_edit(request, id=None):
    item = get_object_or_404(Item,id=id)
    form = ItemForm(request.POST or None, request.FILES or None, instance=item)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.updated_by = request.user
        instance.updated = timezone.now()
        instance.save()
        messages.success(request,"Item saved")
        return redirect('/')

    context = {
        "form": form,
        }
    return render(request,'item_form.html', context)

def item_archive(request):
    today = timezone.now().date()
    queryset = Item.objects.filter(pending=False)

    context = {
        "title":"Archive",
        "object_list": queryset,
        "today": today,
    }
    return render(request,'item_archive.html',context)
