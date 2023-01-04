from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('prod/<id>/', views.prod, name='prod'),
    path('review/', views.review, name='review'),
]
