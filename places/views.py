from django.shortcuts import render
from django.views import View
from .models  import Place
# from .forms import PlaceCommentForm

class PlaceListView(View):
    def get (self,request):
        places=Place.objects.all()
        search_query=request.GET.get("q","")
        if search_query:
            places=Place.objects.filter(name__icontains=search_query)
            
        return render(request, template_name='places/list.html',context={'places':places,'search_query':search_query}) 
        
class PlaceDetailView(View):
     def get(self,request,pk):
        #  form=PlaceCommentForm()
         place=Place.objects.get(pk=pk)
         return render(request,template_name='places/detail.html',context={'place':place})
     
     

