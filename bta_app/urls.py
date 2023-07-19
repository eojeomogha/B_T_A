from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('beats/', views.beats_index, name='index'),
    path('beats/beats/<int:beat_id>/', views.beats_detail, name='detail'),
    path('beats/create', views.BeatCreate.as_view(), name='beats_create'),
    path('beats/<int:pk>/update/', views.BeatUpdate.as_view(), name='beats_update'),
    path('beats/<int:pk>/delete/', views.BeatDelete.as_view(), name='beats_delete'),
    # path('beats/<int:beat_id>/add_beating/', views.add_beating, name='add_beating'),
    # path('signup/', views.signup, name='signup'),
    # path('login/', views.login, name='login'),
    # path('pending/', views.pending, name='pending'),
    # path('completed/', views.completed, name='completed'),
]