from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def feeds(request):
    return render(request, 'feeds.html')

@login_required
def posts(request):
    return render(request, 'posts.html')

@login_required
def subscriptions(request):
    return render(request, 'subscriptions.html')