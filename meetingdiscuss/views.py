from django.shortcuts import render
from .models import AgendaItem

def homepage(request):
    items = AgendaItem.objects.all()
    
    context = {
        'items': items,
    }
    return render(request, "example_page.html", context)
