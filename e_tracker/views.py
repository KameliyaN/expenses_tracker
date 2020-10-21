from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from e_tracker.models import Profile


def home_page(request):
    if request.method == 'POST':
        return render(request, 'e_tracker/home-with-profile.html')
    elif request.method=='GET':
        return render(request, 'e_tracker/home-no-profile.html')
    else:
        return render(request, 'e_tracker/home-with-profile.html')


def create_expense(request):
    return None


def edit_expense(request):
    return None


def delete_expense(request):
    return None


def profile_page(request):
    return None


def profile_edit(request):
    return None


def profile_delete(request):
    return None
