from django.urls import path
from .views import *

urlpatterns = [    
    path('',title),
    path('post/',postOut),
]

#hendler404 = pageNotFound