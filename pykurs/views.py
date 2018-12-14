from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.forms import UserCreationForm


def homepage(request):
    return render(request, 'index.html')


def about(request):
    return HttpResponse('about')

def register(request):
    if request=="POST":
        reg_form = UserCreationForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            return redirect('/login')
    else:
        reg_form = UserCreationForm()
        args = {'reg_form': reg_form}
        return render(request, 'registration_form.html', args)




