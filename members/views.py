from django.shortcuts import render
from django.http import HttpResponse

def members(request): #the name of the view foes not have to be same as the application
    return HttpResponse("Hello world!")