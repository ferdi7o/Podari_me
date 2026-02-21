from django.shortcuts import render, get_object_or_404, redirect
from accounts.models import Profile
from gifts.models import Gift
from .models import Favorite


def index(request):
    profile = Profile.objects.first()
    return render(request, 'interactions/index.html', {'profile': profile})


def toggle_favorite(request, gift_id):
    profile = Profile.objects.first()
    gift = get_object_or_404(Gift, id=gift_id)

    favorite_list, created = Favorite.objects.get_or_create(user_profile=profile)

    if gift in favorite_list.gifts.all():
        favorite_list.gifts.remove(gift)
    else:
        favorite_list.gifts.add(gift)

    return redirect('gift-details', pk=gift_id)


def favorites_list(request):
    profile = Profile.objects.first()
    favorite_obj = Favorite.objects.filter(user_profile=profile).first()

    fav_gifts = favorite_obj.gifts.all() if favorite_obj else []

    context = {
        'fav_gifts': fav_gifts,
        'profile': profile
    }

    return render(request, 'interactions/favorites.html', context)