from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout



def login_view(request):
    
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('')
        else:
            login_form = AuthenticationForm()
    else:
        login_form = AuthenticationForm()


    return render(
        request,
        'login.html',
        {'login': login_form}
    )

def new_user_view(request):
    
    if request.method == 'POST':
        new_user_form = UserCreationForm(request.POST)
        if new_user_form.is_valid():
            new_user_form.save()
            return redirect('login')
        else:
            new_user_form = UserCreationForm()

    else:
        new_user_form = UserCreationForm()

    return render(
        request,
        'new_user.html',
        {'new_user_form': new_user_form}
    )


def logout_view(request):
    logout(request)
    return redirect('')
