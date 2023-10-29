from django.http import HttpResponse

def aboutUs(request):
    return HttpResponse("<h1>This is aboutus page</h1>")