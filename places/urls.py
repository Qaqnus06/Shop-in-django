from django.urls import path
from .views import PlaceListView,PlaceDetailView

app_name='places'


urlpatterns = [
    path('list/',PlaceListView.as_view(), name='list'),
    path('detail/<int:pk>',PlaceDetailView.as_view(), name='detail'),
    

]