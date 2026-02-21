from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from accounts.forms import ProfileCreateForm, ProfileEditForm
from accounts.models import Profile


class ProfileCreateView(View):
    def get(self, request):
        if Profile.objects.exists():
            return redirect('home')
        form = ProfileCreateForm()
        return render(request, 'accounts/profile-create.html', {'form': form})

    def post(self, request):
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'accounts/profile-create.html', {'form': form})


class ProfileDetailView(View):
    def get(self, request):
        profile = Profile.objects.first()
        if not profile:
            return redirect('profile-create')

        all_gifts = profile.gifts.all()
        gifts_count = all_gifts.count()
        gifted_count = all_gifts.filter(status_gift=True).count()

        context = {
            'profile': profile,
            'gifts_count': gifts_count,
            'gifted_count': gifted_count,
        }
        return render(request, 'accounts/profile-details.html', context)


class ProfileEditView(View):
    def get(self, request):
        profile = Profile.objects.first()
        if not profile:
            return redirect('profile-create')

        form = ProfileEditForm(instance=profile)
        return render(request, 'accounts/profile-edit.html', {'form': form})

    def post(self, request):
        profile = Profile.objects.first()
        form = ProfileEditForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('profile-details')

        return render(request, 'accounts/profile-edit.html', {'form': form})


class ProfileDeleteView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'accounts/profile-delete.html')

    def post(self, request):
        profile = Profile.objects.first()
        if profile:
            profile.delete()
        return redirect('home')
