from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from places.models import Comment
from django.views import View


def landing_page(request):
    return render(request, 'landing.html')


class HomeView(LoginRequiredMixin,View):
    def get(self,request):
        place_reviews=Comment.objects.exclude(user=request.user)
        return render(request,'home.html', content_type={'place_reviews':place_reviews})