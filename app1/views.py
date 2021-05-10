from django.shortcuts import render
from django.http import HttpResponse
def TestFun(request):
    return HttpResponse("Hello World")

def AboutFun(request):
    return HttpResponse("<h1>Sample Test run</h1>")

def SamFun(request):
    return render(request,'index.html')
