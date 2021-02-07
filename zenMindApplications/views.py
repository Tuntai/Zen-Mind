from django.shortcuts import render, redirect


# user access restrictions
# decorators for user access restriction
from django.contrib.auth.decorators import login_required


# decorater for restricted access
@login_required(login_url='my_login_url')
# Create your views here.
def meditateAppPage(request):
    my_dict = {}
    return render(request, 'zenMindApplications/meditateApp.html', context=my_dict)


# decorater for restricted access
@login_required(login_url='my_login_url')
# Create your views here.
def priorityListAppPage(request):
    my_dict = {}
    return render(request, 'zenMindApplications/priorityListApp.html', context=my_dict)