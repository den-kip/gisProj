from django.conf.urls import include,url
from gisApp.views import subcounty_datasets , ngo_projects_datasets 
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='user_login'),
    path('home/', views.home, name='user_home'),
    url(r'^subcounty_data/$',subcounty_datasets, name = 'subcounty'),
    url(r'^ngo_projects_data/$',ngo_projects_datasets, name = 'ngoprojs'),
    # path('home/', views.home, name='user_home'),
    # path('home/', views.home, name='n_user_home'),
]
