from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login


def index(request):
    if request.user.is_authenticated:
        #return HttpResponse("is_authenticated "+ str(request.user.username))
        return render(request, 'authapp/index.html')
    else:
        return redirect('login')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)
            return redirect('authapp:index')

    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})
