from django.urls import path

from . import views

urlpatterns = [
    # ex: /player/
    path('', views.index, name='index'),
    # ex: /player/5/
    path('<int:question_id>/', views.detail, name='detail'),
]