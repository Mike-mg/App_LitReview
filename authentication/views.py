from django.shortcuts import render
from django.contrib.auth import authenticate, login
from authentication.forms import LoginForm


def login(request):

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
                message = f'Hello, you are logged as {user.username}.'

            else:
                message = f'Invalids logins'

    return render(request, 'login.html', context={'form': form, 'message': message})