from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    return render(request, 'index.html')

def aboutUs(request):
    return HttpResponse("<h1>This is aboutus page</h1>")

def courses(request):
    return HttpResponse("<h1>This is courses page</h1>")

def singleCourse(request, courseId):
    return HttpResponse(courseId)