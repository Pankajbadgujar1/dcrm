from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.
def home(request):
    #to check see login in
    if request.method == "POST":
        username = request.POST["username"]
    
        password = request.POST["password"]
        

        user = authenticate(username='username',password= password)
        print(user)
        if user is not None:
            login(request, user)
            messages.success(request,"you have successfully log in !")
            redirect('home')

        else:
            messages.success(request,"Errer while you are login ..Please try again")
            
    else:
        return render(request, 'home.html')

def login_user(request):
    pass

def logout_user(request):
    pass