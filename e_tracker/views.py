from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.views import generic

from e_tracker.forms import ProfileForm
from e_tracker.models import Profile, Expense


# @login_required
# def home_page(request):
#     if request.method == 'POST':
#         form = ProfileForm(request.POST)
#         last_name = request.POST.get('last_name')
#         if form.is_valid():
#
#             # if Profile.objects.get(last_name=last_name):
#             try:
#                 profile = Profile.objects.get(last_name)
#                 if profile.expense.all():
#                     context = {
#                         'profile': profile,
#                         'expenses': profile.expense.all()
#                     }
#                     return render(request, 'e_tracker/home-with-profile.html', context)
#                 else:
#                     context = {
#
#                         'expenses': profile.expense.all()
#                     }
#                     return render(request, 'e_tracker/home-with-profile.html', context)
#
#
#             except:
#                 profile = form.save()
#                 profile.save()
#                 context = {'expenses': profile.expense.all()
#                            }
#                 return render(request, 'e_tracker/home-with-profile.html', context)
#     elif request.method == 'GET' and request.GET:
#         profile = Profile(request.GET)
#         context = {'profile': profile}
#
#         return render(request, 'e_tracker/home-with-profile.html', context)
#
#     return render(request, 'e_tracker/home-no-profile.html')
def home_page(request):
    if request.method == 'POST':
        pass

    if request.user.is_authenticated:
       pass
    return render(request, 'e_tracker/home-no-profile.html')


class UserDetail(generic.DetailView):
    model = Profile
    template_name = 'e_tracker/profile.html'
    context_object_name = 'user'


# def redirect_user(request):
#     url = f'e_tracker/profile.html'
#     return HttpResponseRedirect(url)


def create_expense(request):
    return None


def edit_expense(request):
    return None


def delete_expense(request):
    return None


def profile_edit(request):
    return None


def profile_delete(request):
    return None
