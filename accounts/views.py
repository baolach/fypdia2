from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def signup(request):
    # return the page you want to show
    # if they send a post they want to create a username nad password#}

    if request.method == 'POST':
        #user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        if request.POST['password1'] == request.POST['password2']:

            try:
                user = User.objects.get(username =request.POST['username']) # if the user does not have a unique name then they must try again
                return render(request, 'accounts/signup.html', {'error': 'Username has already been taken'})

            except User.DoesNotExist:
                # but if the username is free, then make the user
                user =  User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                login(request, user)
                return render(request, 'accounts/signup.html')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Passwords didn\'t match'})
    else:
        return render(request, 'accounts/signup.html')

    # return render(request, 'accounts/signup.html')