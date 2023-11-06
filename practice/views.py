from django.http import HttpResponse
from django.shortcuts import render

def homePage(request):
    data = {
        'title': 'Home Page template',
        'list': ["Python", 'Javascript', 'Java'],
        'students': [
            { "id": 1, "name": 'test1', "email": 'test1@test.com' },
            { "id": 2, "name": 'test2', "email": 'test2@test.com' },
            { "id": 3, "name": 'test3', "email": 'test3@test.com' },
        ],
        'numbers': [10,20,30,40,50]
    }
    return render(request, 'index.html', data)

def aboutUs(request):
    return render(request, 'aboutus.html')

def courses(request):
    return HttpResponse("<h1>This is courses page</h1>")

def singleCourse(request, courseId):
    return HttpResponse(courseId)