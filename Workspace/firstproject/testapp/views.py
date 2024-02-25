from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
def greetings(request):
    s="<h1>Hello and Welcome to first view</h1>"
    return HttpResponse(s)

def about(request):
    template=loader.get_template('about.html')
    res=template.render()
    return HttpResponse(res)

def contact(request):
    s="<h1>Contact Page</h1>"
    return HttpResponse(s)


