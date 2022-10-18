from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        Cpassword = request.POST['Cpassword']
        
        if password == Cpassword:
            if User.objects.filter(username=username).exists():
                print('Username Taken')
                messages.error(request, 'Username Already Taken!')
                return render(request, 'signup.html')#, {'error': 'Username is already taken!'})
 
            elif User.objects.filter(email=email).exists():
                print('email Taken')
                messages.error(request, 'Email Already Exist!')
                return render(request, 'signup.html')#, {'error':'Email is already taken!'})
                              
            else:
                user = User.objects.create_user(username=username, password=Cpassword, email=email, first_name=first_name, last_name=last_name)
                user.save();
                print('User created')
                auth.login(request,user, backend='django.contrib.auth.backends.ModelBackend')
                return redirect('home')
               
        else:
            print('Password does not match')
            messages.error(request, 'Password Does Not Match!')
            return render(request, 'signup.html')#,{'error': 'Password does not match'})

    else:
        return render(request, 'signup.html')

def login(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            print('logged in')
            messages.success(request, 'Logged Out Succesfully')
            return redirect('home')
        else:
            print('not logged in')
            messages.error(request, 'Incorrect Username or Password!')
            return render(request, 'login.html')#, {'error':  'Username or password is incorrect!'})
            
        
    return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('login')
        
    return render(request, 'logout.html')
# Create your views here.
