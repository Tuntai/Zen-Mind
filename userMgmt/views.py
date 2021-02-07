from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate

# flash messeges
from django.contrib import messages

# for user registration form 
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateMyUserForm

# user login 
from django.contrib.auth import login as auth_login

# user auth and logout
from django.contrib.auth import authenticate, logout 

# to get current user details
from django.contrib.auth import get_user_model


# user access restrictions
# decorators for user access restriction
from django.contrib.auth.decorators import login_required

# Create your views here.

# registerpage from crm app
def register(request):
    form = CreateMyUserForm()
    # when user submits the form
    if request.method == 'POST':
        form = CreateMyUserForm(request.POST)
        # validating the form 
        if form.is_valid():
            new_user = form.save()              # save the form in database
            # showing the success messege in html page
            new_user_name = form.cleaned_data.get('username')

            messages.success(request, 'Account Created for user: ' + new_user_name + "\U0001F604")   
            return redirect('my_login_url')
    my_dict={'form':form,}
    return render(request, template_name='userMgmt/register.html', context=my_dict)



# login page form crm app
def loginPage(request):
    # when user submits data
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        current_user = authenticate(request, username=username, password=password)
        # check if user is in database
        if current_user is not None:
            auth_login(request, current_user)
            return redirect('homePage_url')        # redirect to homepage
        # if wrong user input
        else:
            messages.info(request, 'Username or Password is Incorrect')
    my_dict={}
    return render(request, template_name='userMgmt/login.html', context=my_dict)


# user logout
def logoutUser(request):
    logout(request)
    return redirect('my_login_url')


# decorater for restricted access
@login_required(login_url='my_login_url')
# user page
def userPage(request, primary_key):
    # database query
    User = get_user_model()
    current_user = User.objects.get(id=primary_key)

    my_dict={   'current_user':current_user,
            }
    return render(request, template_name='userMgmt/user.html', context=my_dict)
