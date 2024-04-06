from django.urls import path
from .views import RegisterView ,LoginView,LogoutView,ProfileUpdateView,UserView,SendFriendRequestView,MynetworksView,AcceptFriendRequestView

app_name='user'


urlpatterns = [
    path('register/',RegisterView.as_view(), name='register'),
    path('login/',LoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(), name='logout'),
    path('profile/',ProfileUpdateView.as_view(), name='profile'),
    path('user_list/',UserView.as_view(), name='user_list'),

    path('send_friend/<int:id>/',SendFriendRequestView.as_view(), name='send_friend'),
    path('networks/',MynetworksView.as_view(), name='networks'),
    path('accept_friend/<int:id>/',AcceptFriendRequestView.as_view(), name='accept_friend'),
]