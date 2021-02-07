from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Activity

# order form used in making orders on dashboard
# customized activity form 
class ActivityForm(ModelForm):
    class Meta:
        # model = name of the model for which the form is made
        model = Activity
        # for specific fields=>  fields = ['customer', 'product']
        # or for all fields=>  fields = '__all__'
        fields = '__all__'
        widgets = {
            'activity': forms.Select(attrs={'class': 'activityclass'}),
        }

# print(dir(forms))
