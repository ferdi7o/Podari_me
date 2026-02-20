from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from accounts.models import Profile


class ProfileCreateView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        if Profile.objects.exists():
            return redirect('profile-details')
        return render(request, 'accounts/profile-create.html')


class ProfileDetailView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        profile = Profile.objects.first()
        if not profile:
            return redirect('profile-create')

        context = {
            'profile': profile,
            'gifts_count': profile.gifts.count()
        }
        return render(request, 'accounts/profile-details.html', context)


class ProfileEditView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        profile = Profile.objects.first()
        if not profile:
            return redirect('profile-create')
        return render(request, 'accounts/profile-edit.html', {'profile': profile})


class ProfileDeleteView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'accounts/profile-delete.html')

    def post(self, request):
        profile = Profile.objects.first()
        if profile:
            profile.delete()
        return redirect('home')
