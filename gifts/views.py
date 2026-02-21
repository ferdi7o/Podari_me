from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import GiftCreateForm
from .models import Gift, Tag
from accounts.models import Profile


class DashboardView(View):
    def get(self, request):
        gifts = Gift.objects.all().order_by('-created_at')
        profile = Profile.objects.first()

        all_tags = Tag.objects.all()

        tag_name = request.GET.get('tag')
        if tag_name:
            gifts = gifts.filter(tags__name=tag_name).distinct()

        cat_name = request.GET.get('cat')
        if cat_name:
            gifts = gifts.filter(category=cat_name)

        context = {
            'gifts': gifts,
            'all_tags': all_tags,
            'profile': profile,
            'selected_tag': tag_name,
            'selected_cat': cat_name
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
        current_profile = Profile.objects.first()

        if not current_profile:
            return redirect('profile-create')

        context = {
            'gift': gift,
            'profile': current_profile,
        }
        return render(request, 'gifts/gift_details.html', context)


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



def mark_as_gifted(request, pk):
    if not Profile.objects.exists():
        return redirect('profile-create')

    gift = get_object_or_404(Gift, pk=pk)
    gift.status_gift = True
    gift.save()
    return redirect('gift-details', pk=pk)