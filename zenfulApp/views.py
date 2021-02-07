from django.shortcuts import render

# user access restrictions
# decorators for user access restriction
from django.contrib.auth.decorators import login_required

# Create your views here.


# decorater for restricted access
@login_required(login_url='my_login_url')
# homepage
def homePage(request):
    my_dict={}
    return render(request, template_name='zenfulApp/home.html', context=my_dict)


# decorater for restricted access
@login_required(login_url='my_login_url')
# aboutPage
def aboutPage(request):
    my_dict = {}
    return render(request, template_name='zenfulApp/about.html', context=my_dict)


# decorater for restricted access
@login_required(login_url='my_login_url')
# aboutPage
def activitiesPage(request):
    my_dict = {}
    return render(request, template_name='zenfulApp/activities.html', context=my_dict)


# decorater for restricted access
@login_required(login_url='my_login_url')
# aboutPage
def appsPage(request):
    my_dict = {}
    return render(request, template_name='zenfulApp/apps.html', context=my_dict)


# decorater for restricted access
@login_required(login_url='my_login_url')
# resorce aboutPage
def resourcePage(request):
    my_dict = {}
    return render(request, template_name='zenfulApp/resource.html', context=my_dict)