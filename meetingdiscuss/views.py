from django.shortcuts import render, redirect
from .models import AgendaItem
from .models import SharingItem
from .models import Discuss
from django import forms
#Do I need these?
from django.contrib.auth.models import User
from django.contrib import auth

#class NewUserForm(forms.ModelForm):
#    class Meta:
#        model = User
#        fields = ['username', 'first_name', 'position_title', 'start_date', 'password', 'email']


#class EditUserForm(forms.ModelForm):
#    class Meta:
#        model = User
#        fields = ['username', 'first_name', 'position_title', 'start_date', 'password', 'email']


class DiscussForm(forms.ModelForm):
    class Meta:
        model = Discuss
        fields = ['text', 'image']
        
class ShareForm(forms.ModelForm):
    class Meta:
        model = SharingItem
        fields = ['text', 'image'] 
        
def homepage(request):
    return redirect('/accounts/login/')
               

def discussion(request):
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
    
def thread(request, given_id):
    discuss_items = Discuss.objects.all()
    # Uncomment this when you add an agenda_item foreign key
    # discuss_items = discuss_items.filter(agenda_item_id=given_id)
    print(list(discuss_items))
    context = {
    }
    
    
    return render(request, "thread.html", context)
    
    
    
