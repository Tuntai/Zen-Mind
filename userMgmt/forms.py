# from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

# from .models import Order

# order form used in making orders on dashboard
# class OrderForm(ModelForm):
#     class Meta:
#         # model = name of the model for which the form is made
#         model = Order
#         # for specific fields=>  fields = ['customer', 'product']
#         # or for all fields=>  fields = '__all__'
#         fields = '__all__'

# creating a custom form for registration
class CreateMyUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']