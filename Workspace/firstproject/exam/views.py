from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
def testpaper(request):
    que="who developed Python?"
    a="Dennis Richie"
    b="Guido van Rousom"
    c="Ken Thomsan"
    d="Bajarne Stroustrup"
    context={
        'que':que,
        'options':[a,b,c,d]

    }
    template=loader.get_template('testpaper.html')
    res=template.render(context,request)
    return HttpResponse(res)

def result(request):
    s="<h1>Result</h1>"
    return HttpResponse(s)

