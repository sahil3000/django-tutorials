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
    return render(request, 'home.html', data)

def aboutUs(request):
    return render(request, 'aboutus.html')

def courses(request):
    data = {}
    if request.method == 'GET':
        print("innnnnnnnnn")
        name = request.GET.get('name', "") # way1
        fee = request.GET.get('fee', "")    # way2
        # fee = request.GET["fee"]    # way2
        data["name"] = name
        data["fee"] = fee
    print(data)
    return render(request, 'course.html', data)

def contactUs(request):
    data = {"isSubmit": False}
    isSubmit = False
    if (request.method == 'POST'):
        name = request.POST.get('name', '')
        msg = request.POST.get('msg', '')
        data["name"] = name
        data["msg"] = msg
        data["isSubmit"] = True
    return render(request, 'contact-us.html', data)

def singleCourse(request, courseId):
    return HttpResponse(courseId)