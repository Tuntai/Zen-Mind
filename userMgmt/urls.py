from django.urls import path
# from userMgmt.core import views as core_views
from .views import userPage, register, loginPage, logoutUser


urlpatterns = [
    # register url
    path('register/', register, name="register_url"),
    # login url
    path('login/', loginPage, name="my_login_url"),
    # logout url
    path('logout/', logoutUser, name="logout_url"),

    path('user/<str:primary_key>/', userPage, name="userPage_url"),
    # path('customer/<str:primary_key>/', views.customer, name="customer_url"),
]