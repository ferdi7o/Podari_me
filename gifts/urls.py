from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('create/', views.GiftCreateView.as_view(), name='gift-create'),

]