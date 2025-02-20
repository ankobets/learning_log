from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrForm, UserUpdateForm, ProfileFillForm
from .models import Profile


# Create your views here.

def register(request):
    if request.method != 'POST':
        form = UserRegistrForm()

    else:
        form = UserRegistrForm(request.POST, request.FILES)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('learning_logs:index')

    context = {'form': form}
    return render(request, 'registration/register.html', context)


def profile(request):
    return render(request, 'registration/profile.html')


def edit_profile(request):
    print(request.method)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileFillForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect('users:profile')

    else:
        print(request.user)
        print(request.user.profile )
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileFillForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'registration/edit_profile.html', context)

