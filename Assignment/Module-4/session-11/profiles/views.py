from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import InfluencerProfile
from .forms import InfluencerProfileForm

def get_current_or_demo_user(request):
    if request.user.is_authenticated:
        return request.user
    user, created = User.objects.get_or_create(username='demo_influencer')
    if created:
        user.set_password('password123')
        user.save()
    return user

def profile_view(request):
    user = get_current_or_demo_user(request)
    profile, created = InfluencerProfile.objects.get_or_create(user=user)
    return render(request, 'profiles/profile_detail.html', {'profile': profile})

def profile_edit_view(request):
    user = get_current_or_demo_user(request)
    profile, created = InfluencerProfile.objects.get_or_create(user=user)

    if request.method == 'POST':
        form = InfluencerProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile_view')
        else:
            messages.error(request, 'Please fix the errors highlighted below.')
    else:
        form = InfluencerProfileForm(instance=profile)

    return render(request, 'profiles/profile_edit.html', {'form': form, 'profile': profile})
