from django.urls import path

from . import views

urlpatterns = [
    # ex: /player/
    path('', views.list, name='list'),
    # ex: /player/5/
    path('<str:player_id>/', views.detail, name='detail'),
]