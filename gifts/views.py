from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from .forms import GiftCreateForm
from .models import Gift
from accounts.models import Profile


class DashboardView(View):
    def get(self, request):
        gifts = Gift.objects.all().order_by('-created_at') #Take new gift first!
        profile = Profile.objects.first()
        context = {
            'gifts': gifts,
            'profile': profile
        }
        return render(request, 'gifts/dashboard.html', context)


class GiftCreateView(View):
    def get(self, request):
        if not Profile.objects.exists():
            return redirect('profile-create')
        form = GiftCreateForm()
        return render(request, 'gifts/gift-create.html', {'form': form})

    def post(self, request):
        form = GiftCreateForm(request.POST)
        if form.is_valid():
            gift = form.save(commit=False)
            gift.owner = Profile.objects.first()
            gift.save()
            form.save_m2m()
            return redirect('dashboard')
        return render(request, 'gifts/gift-create.html', {'form': form})


class GiftDetailView(View):
    def get(self, request, pk):
        gift = get_object_or_404(Gift, pk=pk)
        return render(request, 'gifts/gift_details.html', {'gift': gift})


class GiftEditView(View):
    def get(self, request, pk):
        gift = get_object_or_404(Gift, pk=pk)
        form = GiftCreateForm(instance=gift)
        return render(request, 'gifts/gift-edit.html', {'form': form, 'gift': gift})

    def post(self, request, pk):
        gift = get_object_or_404(Gift, pk=pk)
        form = GiftCreateForm(request.POST, instance=gift)
        if form.is_valid():
            form.save()
            return redirect('gift-details', pk=gift.pk)
        return render(request, 'gifts/gift-edit.html', {'form': form, 'gift': gift})


class GiftDeleteView(View):
    def get(self, request, pk):
        gift = get_object_or_404(Gift, pk=pk)
        return render(request, 'gifts/gift-delete.html', {'gift': gift})

    def post(self, request, pk):
        gift = get_object_or_404(Gift, pk=pk)
        gift.delete()
        return redirect('dashboard')
