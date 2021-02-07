from django.shortcuts import render, redirect

# for User Model
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

# for Activity Selection form
from django.forms import inlineformset_factory
from .forms import Activity

# user access restrictions
# decorators for user access restriction
from django.contrib.auth.decorators import login_required


# Create your views here.

# decorater for restricted access
@login_required(login_url='my_login_url')
def userProfilePage(request, primary_key):
    User = get_user_model()
    # database query
    User = get_user_model()
    current_user = User.objects.get(id=primary_key)
    # database quert
    # to get all activities by current user
    # activitiesUser
    current_user_activities = current_user.activity_set.all().order_by('-id')
    total_current_user_activities = current_user_activities.count
    my_dict={   'current_user':current_user,
                'current_user_activities': current_user_activities,
                'total_current_user_activities': total_current_user_activities,
            }
    return render(request, template_name='userDataApp/userProfile.html', context=my_dict)



# decorater for restricted access
@login_required(login_url='my_login_url')
# model to handle create Activity on dashboard
def selectActivity(request, primary_key):
    # inline form set - parameters: inlineformset_factory(parentModel, childModel, fields=fields to show)
    ActivityFormSet = inlineformset_factory(User, Activity, fields=('activity',), extra=1)
    # individual customer
    individual_user = User.objects.get(id=primary_key)
    # passing the form
    # queryset=Order.objects.none() - does not displays the selected orders in view
    formset = ActivityFormSet(queryset=Activity.objects.none(), instance=individual_user)
    # when user submits form
    if request.method == 'POST':
        # print('PRINTING new ORDER', request.POST)
        # get all the Post data   
        formset = ActivityFormSet(request.POST, instance=individual_user)
        if formset.is_valid():                 # check if the form is valid
            formset.save()                     # save the form in database
            return redirect(f'/userProfile/{primary_key}/')            # redirect user to homepage
    my_dict = { 'formset': formset,
                'individual_user': individual_user,
            }

    # html page present in userDataApp
    return render(request, 'userDataApp/newActivities.html', context=my_dict)
