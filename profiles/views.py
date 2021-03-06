from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import UserProfile
from .forms import UserProfileForm


@login_required
def profile(request):
    """
    Display user profile
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Successfully Updated')
        else:
            messages.error(request,
                           'Update failed, please check form is valid')
    else:
        form = UserProfileForm(instance=profile)
        orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders
    }

    return render(request, template, context)
