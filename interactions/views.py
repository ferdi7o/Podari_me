from django.shortcuts import render
from accounts.models import Profile

def index(request):
    profile = Profile.objects.first()
    return render(request, 'interactions/index.html', {'profile': profile})