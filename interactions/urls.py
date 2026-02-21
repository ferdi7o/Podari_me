from django.urls import path
from . import views
from .views import toggle_favorite

app_name = 'interactions'
urlpatterns = [
    path('', views.index, name='home'),
    path('favorite/<int:gift_id>/', toggle_favorite, name='toggle-favorite'),
    path('my-favorites/', views.favorites_list, name='favorites-list'),
]
