from django.shortcuts import render

# Create your views here.

def page_feedback(request):
    return render(request,"feedback.html")