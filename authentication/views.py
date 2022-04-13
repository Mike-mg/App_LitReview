from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from authentication.forms import LoginForm, SignUpForm


def login_page(request):

    form = LoginForm()
    message = ''

    if request.method == 'POST':

        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )

            if user is not None:
                login(request, user)
                return redirect('home')

            else:
                message = f'Invalids logins'

    return render(request, 'login.html', context={'form': form, 'message': message})

def logout_user(request):
    logout(request)
    return redirect('login')

def signup_page(request):

    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            redirect('home')

    return render(request, 'signup.html', context={'form': form})