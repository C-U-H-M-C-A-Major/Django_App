from django.shortcuts import render
from django.http import HttpResponse

def testpaper(request):
    s="<h1>This is a test paper</h1>"
    return HttpResponse(s)

def result(request):
    s="<h1>Result</h1>"
    return HttpResponse(s)

