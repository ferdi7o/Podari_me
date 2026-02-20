from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.ProfileCreateView.as_view(), name='profile-create'),
    path('details/', views.ProfileDetailView.as_view(), name='profile-details'),
    path('edit/', views.ProfileEditView.as_view(), name='profile-edit'),
    path('delete/', views.ProfileDeleteView.as_view(), name='profile-delete'),
]