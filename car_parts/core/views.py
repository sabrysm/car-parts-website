from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from part.models import Part

def index(request):
    user = User.objects.get(username='caravella')
    parts = Part.objects.all()
    
    return render(request, 'core/index.html', {
        "user": user,
        "parts": parts
    })


def parts(request):
    return render(request, 'core/parts.html')

def search(request):
    return render(request, 'core/search.html')


def logout_view(request):
    logout(request)
    return redirect('core:login')

