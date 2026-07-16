Django Views are python functions that take http requests and return http responses like HTML documents. A webpage that uses Django is full of views with different tasks and missions. They are usually in views.py in your app folder.
<br>
Example for the members app <br>
from django.shortcuts import render
from django.http import HttpResponse

def members(request): #the name of the view foes not have to be same as the application
    return HttpResponse("Hello world!")

#### URLs
1. Create a file named urls.py in the same folder as views.py, then <br>
from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
] <br>

There is a file called urls.py in the project folder. Open it and ad the include module in the import statement, and also add a path() function in the urlpatters[] list, with arguments that will route users that come in via 127.0.0.1:8000/