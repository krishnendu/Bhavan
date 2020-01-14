from django.urls import include,path
from django.conf.urls import url
from . import views
from django.contrib.auth import login #, logout

urlpatterns = [
    
    path('',views.home, name='home'),
    path('register/',views.register, name='register'),
    path('login/', views.login_view,  name='login'),
    path('logout/',views.logout_view, name='logout'),
    path('<str:username>/',views.profile, name='profile'),
    path('<str:username>/feedback',views.feedback_view, name='feedback'),
    path('<str:username>/edit',views.editprofile, name='editprofile'),
]
