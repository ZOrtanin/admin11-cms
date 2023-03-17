from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from .views import *

app_name = 'landing'


urlpatterns = [    
    path('',LandingHome.as_view(),name='home'),
    path('post/',postOut,name='postform'),

    path('login/',LoginUser.as_view(),name='login'),
    path('signup/',RegisterUser.as_view(),name='signup'),
    path('logout/',logout_user,name='logout'),

    path('dashboard/',DashboardPage.as_view(),name='dashboard'),
    path('edit/',EditMode.as_view(),name='edit'),
    path('edit/block/<int:id_block>/',EditBlock.as_view(),name='edit_block'),
    path('edit/published/<int:id_block>/',EditModeDisableBlock,name='published'),
    path('sorting/',SortingHome.as_view(),name='sorting'),
   
    path('sort/',sort_blocks),

    path('orders/',OrderPage.as_view(),name='order'),
    path('orders/<int:order_id>/',getOrderOut,name='order_id'),
    path('orders/edit/<int:order_id>/',OrderEdit,name='order_id_edit'),
    path('orders/del/<int:order_id>/',OrderDel,name='order_id_del'),


    path('users/',UsersPage.as_view(),name='users'),
    path('files/',FilesPage.as_view(),name='files'),

    #path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
]

#hendler404 = pageNotFound