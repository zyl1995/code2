from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return HttpResponse("Rango says hey there world!<br/> <a href='/rango/about'>About</a>")
    context_dict ={'boldmessage':'I am bold font from the context'}
    return render(request,'rango/index.html',context_dict)
def about(request):
    #return HttpResponse("Rango says here is the about page<br/> <a href='/rango'>Index</a>")
    context_dict={'himessage':'I am about something from rango'}
    #return render(request,'rango/about.html',context_dict)
    #context_dict ={'himessage':'I am bold font from the context1111'}
    return render(request,'rango/about.html',context_dict)