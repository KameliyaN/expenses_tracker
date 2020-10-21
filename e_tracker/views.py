from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from e_tracker.forms import ProfileForm
from e_tracker.models import Profile


def home_page(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            person = form.save()
            person.save()
            context={
                'form':form
            }
            return render(request, 'e_tracker/profile.html',context)
    else:
        smtng = request.GET.get(profile_page(request))
        if smtng:
            return render(request, 'e_tracker/home-with-profile.html')
        return render(request, 'e_tracker/home-no-profile.html')


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
