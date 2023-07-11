from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from . import views
from django.urls import reverse


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('exercises/', views.exercise_index, name='index'),
    path('exercises/<int:exercise_id>/', views.exercise_detail, name='detail'),
    path('exercises/create/', views.ExerciseCreate.as_view(), name='exercises_create'),
    path('exercises/<int:pk>/update/', views.ExerciseUpdate.as_view(), name='exercises_update'),
    path('exercises/<int:pk>/delete/', views.ExerciseDelete.as_view(), name='exercises_delete'),
    #API
    # path('exercises/search', include('rest_framework.urls')),
    path('exercises/search', views.exercise_searches, name='exercises_searches'),
]