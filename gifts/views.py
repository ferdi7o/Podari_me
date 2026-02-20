from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
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
        return render(request, 'gifts/gift-create.html')



class GiftDetailView(View):
    def get(self, request, pk):
        gift = get_object_or_404(Gift, pk=pk)
        return render(request, 'gifts/gift-details.html', {'gift': gift})
