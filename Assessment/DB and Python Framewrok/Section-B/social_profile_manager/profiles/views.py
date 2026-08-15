from django.shortcuts import render, redirect
from .forms import UserProfileForm
from .models import UserProfile
import csv
import os
from django.conf import settings

from django.http import HttpResponse
# Create your views here.


def create_profile(request):

    if request.method == 'POST':
        form = UserProfileForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('profile_list')

    else:
        form = UserProfileForm()

    return render(
        request,
        'profiles/create_profile.html',
        {'form': form}
    )


def profile_list(request):

    profiles = UserProfile.objects.all()

    return render(
        request,
        'profiles/profile_list.html',
        {'profiles': profiles}
    )


def edit_profile(request, id):

    profile = UserProfile.objects.get(id=id)

    if request.method == 'POST':
        form = UserProfileForm(
            request.POST,
            instance=profile
        )

        if form.is_valid():
            form.save()
            return redirect('profile_list')

    else:
        form = UserProfileForm(instance=profile)

    return render(
        request,
        'profiles/edit_profile.html',
        {
            'form': form,
            'profile': profile
        }
    )
def export_profiles(request):

    profiles = UserProfile.objects.all()

    file_path = os.path.join(
        settings.BASE_DIR,
        'profiles.csv'
    )

    with open(
        file_path,
        'w',
        newline='',
        encoding='utf-8'
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            'ID',
            'Username',
            'Age',
            'Public'
        ])

        for profile in profiles:

            writer.writerow([
                profile.id,
                profile.username,
                profile.age,
                profile.is_public
            ])

    with open(file_path, 'rb') as file:

        response = HttpResponse(
            file.read(),
            content_type='text/csv'
        )

    response['Content-Disposition'] = (
        'attachment; filename="profiles.csv"'
    )

    return response