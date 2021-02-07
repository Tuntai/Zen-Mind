from django.urls import path
from .views import userProfilePage, selectActivity

urlpatterns = [
    path('userProfile/<str:primary_key>/', userProfilePage, name="userProfilePage_url"),

    # uds = userdataHistory
    path('selectactivity/<str:primary_key>/', selectActivity, name="selectActivity_url"),


]