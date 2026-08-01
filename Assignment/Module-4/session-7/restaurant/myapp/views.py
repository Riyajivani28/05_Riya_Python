from django.shortcuts import render, redirect
from .forms import RestaurantForm

def add_restaurant(request):
    if request.method == "POST":
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_restaurant')  # Redirect after successful save
    else:
        form = RestaurantForm()

    return render(request, 'add_restaurant.html', {'form': form})