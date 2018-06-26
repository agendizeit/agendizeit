from django.shortcuts import render, redirect
from .models import AgendaItem
from .models import SharingItem
from .models import Discuss
from django import forms
#Do I need these?
#from django.contrib.auth.models import User
#from django.contrib import auth

class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'position_title', 'start_date', 'password', 'email']


class EditUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'position_title', 'start_date', 'password', 'email']


class DiscussForm(forms.ModelForm):
    class Meta:
        model = Discuss
        fields = ['text', 'image']
        
class ShareForm(forms.ModelForm):
    class Meta:
        model = Share
        fields = ['text', 'image'] 
        
def homepage(request):
    if request.method == 'POST':

        form = NewUserForm(request.POST)

        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect('/')

    else:
        form = NewUserForm()

    context = {
        'form': form,
    }
    return render(request, 'home.html', context)
               

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
    
    
