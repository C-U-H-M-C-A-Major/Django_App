# user defined views
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
    #return HttpResponse("hello")

def analyze(request):
    djtext=request.GET.get('text','default')
    removepunc=request.GET.get('removepunc','off')
    fullcaps=request.GET.get('fullcaps','off')
    newlineremover=request.GET.get('newlineremover','off')
    smallcaps=request.GET.get('smallcaps','off')

    if removepunc=="on":
        punctuations= '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
    
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char

        params={'purpose':'Removed Punctuations', 'analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    
    elif(fullcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+ char.upper()
        
        
        params={'purpose':'UPPERCASE', 'analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    
    elif(newlineremover=="on"):
        analyzed=""
        for char in djtext:
            if char !='\n':
                analyzed=analyzed+ char
        
        
        params={'purpose':'New Line Remover', 'analyzed_text':analyzed}
        return render(request,'analyze.html',params)
    
    elif(smallcaps=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+ char.lower()
        
        
        params={'purpose':'lowercase', 'analyzed_text':analyzed}
        return render(request,'analyze.html',params)

    else:
        return HttpResponse("Error")
    

'''def capfirst(request):
    return HttpResponse("captialize")

def newlineremove(request):
    return HttpResponse("new line")

def spaceremove(request):
    return HttpResponse("space remove")

def charcount(request):
    return HttpResponse("char count<a href='/'>back</a>")
'''