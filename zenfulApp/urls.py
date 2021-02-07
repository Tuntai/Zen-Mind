from django.urls import path
from .views import homePage, aboutPage, activitiesPage, appsPage, resourcePage

urlpatterns = [
    path('', homePage, name="homePage_url"),
    path('about/', aboutPage, name="aboutPage_url"),
    path('activities/', activitiesPage, name="activitiesPage_url"),
    path('apps/', appsPage, name="appsPage_url"),
    path('resource/', resourcePage, name="resourcePage_url"),
]