from django.conf.urls import include,url
from gisApp.views import subcounty_datasets , ngo_projects_datasets
from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # path('', views.login, name='user_login'),
    url('^$', auth_views.LoginView.as_view(template_name="gisApp/login.html"), name='login'),
    path('home/', views.home, name='user_home'),
    path('donors/', views.donors, name='donors'),
    path('Institutions/', views.inst, name='inst'),
    url(r'^subcounty_data/$',subcounty_datasets, name = 'subcounty'),
    url(r'^ngo_projects_data/$',ngo_projects_datasets, name = 'ngoprojs'),
    # path('home/', views.home, name='user_home'),
    # path('home/', views.home, name='n_user_home'),
]
