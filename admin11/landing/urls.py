from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *

app_name = 'landing'


urlpatterns = [    
    path('',LandingHome.as_view()),
    path('dashboard/',DashboardPage.as_view()),
    path('sorting/',SortingHome.as_view()),
    path('post/',postOut),
    path('sort/',sort_blocks),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
]

#hendler404 = pageNotFound