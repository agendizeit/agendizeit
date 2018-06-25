from django.shortcuts import render
from .models import AgendaItem
from .models import SharingItem

def homepage(request):
    items = AgendaItem.objects.all()
    context = {
        'items': items,
    }
    return render(request, "discussion.html", context)

def sharing(request):
    sitems = SharingItem.objects.all()
    context = {
        'sitems': sitems,
    }
    print(context)
    return render(request, "sharing.html", context)
