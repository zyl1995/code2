from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Lategory
from rango.models import Page

def index(request):
    # return HttpResponse("Rango says hey there world!<br/> <a href='/rango/about'>About</a>")
    #context_dict ={'boldmessage':'I am bold font from the context'}
    #return render(request,'rango/index.html',context_dict)
    category_list = Lategory.objects.order_by('-likes')[:5]
    context_dict = {'categories':category_list}
    return  render(request,'rango/index.html',context_dict)

def about(request):
    #return HttpResponse("Rango says here is the about page<br/> <a href='/rango'>Index</a>")
    context_dict = {'himessage':'I am about something from rango11'}
    #return render(request,'rango/about.html',context_dict)
    #context_dict ={'himessage':'I am bold font from the context1111'}
    return render(request,'rango/about.html',context_dict)

def category(request, category_name_slug):

    context_dict = {}

    try:
        category = Lategory.objects.get(slug=category_name_slug)
        context_dict['category_name'] = category.name
        pages=Page.objects.filter(category=category)
        context_dict['pages']=pages
        context_dict['category']=category
    except Lategory.DoesNoExist:
        pass

    return render(request, 'rango/category.html', context_dict)

