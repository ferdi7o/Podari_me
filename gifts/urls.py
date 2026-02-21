from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('create/', views.GiftCreateView.as_view(), name='gift-create'),
    path('details/<int:pk>/', views.GiftDetailView.as_view(), name='gift-details'),
    path('edit/<int:pk>/', views.GiftEditView.as_view(), name='gift-edit'),
    path('delete/<int:pk>/', views.GiftDeleteView.as_view(), name='gift-delete'),
]
