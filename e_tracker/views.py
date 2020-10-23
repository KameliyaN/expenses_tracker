from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.views import generic

from e_tracker.forms import ProfileForm, ExpenseForm
from e_tracker.models import Profile, Expense


# @login_required
def home_page(request, pk=None):
    if request.method == 'POST':
        form = ProfileForm(request.POST)

        last_name = request.POST.get('last_name')
        if form.is_valid():

            # if Profile.objects.get(last_name=last_name):
            try:
                profile = Profile.objects.get(last_name)
                if profile.expense.all():
                    context = {
                        'profile': profile,
                        'expenses': profile.expense.all()
                    }
                    return render(request, 'e_tracker/home-with-profile.html', context)
                else:
                    context = {

                        'expenses': profile.expense.all()
                    }
                    return render(request, 'e_tracker/home-with-profile.html', context)


            except:
                profile = form.save()
                profile.save()
                context = {'expenses': profile.expense.all()

                           }
        return render(request, 'e_tracker/home-with-profile.html')

    elif request.method == 'GET':
        profile = Profile(request.GET).id

        context = {'profile': profile}
        if profile:
            return render(request, 'e_tracker/home-with-profile.html', context)

        return render(request, 'e_tracker/home-no-profile.html')


def create_expense(request, pk=None):
    print(request.GET[pk])
    if request.method == "POST":
        form = ExpenseForm(request.POST)

        profile = get_object_or_404(Profile, pk=pk)

        if form.is_valid():
            created_expense = form.save()

            profile.expense.add(created_expense)
            created_expense.save()
            context = {
                'created_expense': created_expense
            }
            return render(request, 'e_tracker/home-with-profile.html', context)
    return render(request, 'e_tracker/expense-create.html')


def edit_expense(request):
    return None


def delete_expense(request):
    return None


def profile_edit(request):
    return None


def profile_delete(request):
    return None


def profile(request):
    return None
