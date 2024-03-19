from django.urls import path
from .views import RegisterView ,LoginView

app_name='user'


urlpatterns = [
    path('register/',RegisterView.as_view(), name='register'),
    path('login/',LoginView.as_view(), name='login'),
    
    # path('logout/', views.logout, name='logout'),
    

]