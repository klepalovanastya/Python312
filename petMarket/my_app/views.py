from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def page1(request):
    return HttpResponse("страница появилась!!!")

def page2(request):
    return HttpResponse("вторая страница появилась")
