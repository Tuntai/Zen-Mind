from django.urls import path
from .views import meditateAppPage, priorityListAppPage

urlpatterns = [
    path('apps/meditate', meditateAppPage, name="meditateAppPage_url"),
    path('apps/prioritylist/', priorityListAppPage, name="priorityListAppPage_url"),
]