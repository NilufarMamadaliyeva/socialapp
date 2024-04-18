from django.urls import path
from .views import login,get_user_info,register_user
from knox import views as knox_views

urlpatterns = [
    path('login/', login, name='login'),
    path('get_user_info/', get_user_info, name='get_user_info'),
    path('register/', register_user, name='register'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]