from django.urls import path
from users import views


app_name = 'users'
urlpatterns = [
    path('', views.home, name='home'),
    path('login_page/', views.login_view, name='login_page'),
    path('make_user/', views.make_user, name='make_user'),
    path('profile_page/', views.profile_page, name='profile_page'),
    path('logout/', views.logout, name='logout'),
    path('user/follow/<int:id>/', views.user_follow, name='user-follow'),
    path('', views.home, name='home'),
]
