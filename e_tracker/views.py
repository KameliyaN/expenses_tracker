from django.shortcuts import render


# Create your views here.
def home_page(request):
    return render(request,'e_tracker/home-no-profile.html')


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