from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    data = {
        'title': 'Home Page template'
    }
    return render(request, 'index.html', data)

def aboutUs(request):
    return HttpResponse("<h1>This is aboutus page</h1>")

def courses(request):
    return HttpResponse("<h1>This is courses page</h1>")

def singleCourse(request, courseId):
    return HttpResponse(courseId)