from django.shortcuts import render,redirect
from django .views import View
from .forms import RegisterForm,LoginForm,ProfileUpdateForm
from django.contrib.auth import authenticate
from django.contrib.auth .mixins import LoginRequiredMixin
from django.contrib.auth import logout,login
from django.contrib  import  messages
from .models import User,FriendRequest  


class LoginView(View):
    def get(self, request):  

        form = LoginForm()
        return render(request,'login.html',context={'form':form})
    
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
         
            user=authenticate(username=username ,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,"siz muvaffaqiyatli kirdingiz")

            return redirect('landing_page')
        return render(request,'login.html',context={'form':form})    
class LogoutView(LoginRequiredMixin,View):
    def get(self, request):
        logout(request)
        messages.success(request,"siz muvaffaqiyatli  logout qildingiz")
        return redirect('landing_page') 


    

class RegisterView(View):
    def get(self, request):  

        form = RegisterForm()
        return render(request,'register.html',context={'form':form})
    

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('landing_page')
        else:
            return render(request,'register.html',context={'form':form})


class ProfileUpdateView(LoginRequiredMixin,View):

    def get (self,request):
        form=ProfileUpdateForm(instance=request.user)
        return render(request,'profile.html',{'form':form})
    

    def post(sellf,request):
        form=ProfileUpdateForm(instance=request.user,data=request.POST, files=request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request,"muvaffaqiyatli kiridingiz")
            return redirect('places:list')
        
        return render(request,'profile.html',{'form':form})
class UserView(LoginRequiredMixin,View):
    def get(self,request):
        user=User.objects.exclude(username=request.user.username)   
        friend_requests=FriendRequest.objects.filter(to_user=request.user) 

        return render(request,'user_list.html',{'user':user,"friend_requests":friend_requests})
    


class MynetworksView(LoginRequiredMixin,View):
    def get(self,request):
        networks=FriendRequest.objects.filter(to_user=request.user, is_accepted=False)


        return render(request,'user/networks_list.html',{'networks':networks})


class AcceptFriendRequestView(LoginRequiredMixin,View):
    def get(self,request,id):
        friend_request=FriendRequest.objects.get(id=id)
        from_user=friend_request.from_user
        main_user=request.user

        main_user.friends.add(from_user)
        from_user.friends.add(main_user)

        friend_request.is_accepted=True
        friend_request.save()
        return redirect('user:my_networks')


class SendFriendRequestView(LoginRequiredMixin,View,id):
    def get(self,request,id):
        to_user=User.objects.get(id=id)
        from_user=request.user

        FriendRequest.objects.get_or_create(from_user=from_user, to_user=to_user)

       
        return redirect('user:user_list')


