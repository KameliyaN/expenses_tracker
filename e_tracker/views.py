from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.views import generic

from e_tracker.forms import ProfileForm, ExpenseForm
from e_tracker.models import Profile, Expense


def home_page(request):
    if not len(Profile.objects.all()):
        if request.method == 'GET':
            context = {
                'form': ProfileForm()
            }
            return render(request, 'e_tracker/home-no-profile.html', context)
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'e_tracker/home-no-profile.html', {'form': ProfileForm()})
    else:
        expenses = False if len(Expense.objects.all()) == 0 else Expense.objects.all()
        budget = Profile.objects.first().budget
        prices = [i.price for i in Expense.objects.all()]
        left = budget - sum(prices)
        context = {
            'expenses': expenses,
            'budget': budget,
            'prices': prices,
            'left': left,
        }
        return render(request, 'e_tracker/home-with-profile.html', context)
    # context = {
    #     'form': ProfileForm(),
    #     'expense': Expense.objects.all()}
    #
    # if request.method == 'GET':
    #     prof = Profile.objects.all()
    #     if not prof:
    #         return render(request, 'e_tracker/home-with-profile.html', context)
    #     return render(request, 'e_tracker/home-with-profile.html', context)

    # if request.method == 'POST':
    #
    #     form = ProfileForm(request.POST)
    #
    #     last_name = request.POST.get('last_name')
    #
    #     if form.is_valid():
    #
    #         # if Profile.objects.get(last_name=last_name):
    #         try:
    #             profile = Profile.objects.get(last_name)
    #             if profile.expense.all():
    #                 context = {
    #                     'profile': profile,
    #                     'expenses': profile.expense.all()
    #                 }
    #                 return render(request, 'e_tracker/home-with-profile.html', context)
    #             else:
    #                 context = {
    #
    #                     'expenses': profile.expense.all()
    #                 }
    #                 return render(request, 'e_tracker/home-with-profile.html', context)
    #
    #
    #         except:
    #             profile = form.save()
    #             profile.save()
    #             context = {'expenses': profile.expense.all()
    #
    #                        }
    #     return render(request, 'e_tracker/home-with-profile.html')
    #
    # elif request.method == 'GET':
    #     profile = Profile(request.GET).id
    #
    #     context = {'profile': profile}
    #     if profile:
    #         return render(request, 'e_tracker/home-with-profile.html', context)
    #
    #     return render(request, 'e_tracker/home-no-profile.html')


def create_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)

        if form.is_valid():
            prof = Profile.objects.first()
            form.prof = form.save()
            form.prof.save()
            expenses = False if len(Expense.objects.all()) == 0 else Expense.objects.all()
            budget = Profile.objects.first().budget
            prices = [i.price for i in Expense.objects.all()]
            left = budget - sum(prices)
            context = {
                'expenses': expenses,
                'budget': budget,
                'prices': prices,
                'left': left,
            }

            return render(request, 'e_tracker/home-with-profile.html', context)

        # return render(request, 'e_tracker/expense-create.html', {'form': form})
    form = ExpenseForm()
    return render(request, 'e_tracker/expense-create.html', {'form': form})


def edit_expense(request, pk):
    expense = Expense.objects.get(pk=pk)

    if request.method == 'GET':
        form = ExpenseForm(instance=expense)
        context = {
            'expense': expense,
            'form': form
        }
        return render(request, 'e_tracker/expense-edit.html', context)
    form = ExpenseForm(request.POST, instance=expense)
    if form.is_valid():
        form.prof = form.save()
        form.prof.save()
        expenses = False if len(Expense.objects.all()) == 0 else Expense.objects.all()
        budget = Profile.objects.first().budget
        prices = [i.price for i in Expense.objects.all()]
        left = budget - sum(prices)
        context = {
            'expenses': expenses,
            'budget': budget,
            'prices': prices,
            'left': left,
        }

        return render(request, 'e_tracker/home-with-profile.html', context)


def delete_expense(request, pk):
    expense = Expense.objects.get(pk=pk)

    if request.method == 'GET':
        form = ExpenseForm(instance=expense)
        context = {
            'expense': expense,
            'form': form
        }
        return render(request, 'e_tracker/expense-delete.html', context)

    expense.delete()
    expenses = False if len(Expense.objects.all()) == 0 else Expense.objects.all()
    budget = Profile.objects.first().budget
    prices = [i.price for i in Expense.objects.all()]
    left = budget - sum(prices)
    context = {
        'expenses': expenses,
        'budget': budget,
        'prices': prices,
        'left': left,
    }

    return render(request, 'e_tracker/home-with-profile.html', context)


def profile_edit(request):
    profile = Profile.objects.first()
    if request.method == 'GET':
        context = {
            'form': ProfileForm(instance=profile),
            'profile': profile
        }
        return render(request, 'e_tracker/profile-edit.html', context)
    form = ProfileForm(request.POST, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('profile')


def profile_delete(request):
    profile = Profile.objects.first()
    if request.method == 'GET':
        return render(request, 'e_tracker/profile-delete.html')
    profile.delete()
    return redirect('home')


def profile(request):
    budget = Profile.objects.first().budget
    prices = [i.price for i in Expense.objects.all()]
    left = budget - sum(prices)
    context = {
        'form': ProfileForm(request.GET),
        'profile': Profile.objects.first(),
        'left': left

    }
    return render(request, 'e_tracker/profile.html', context)
