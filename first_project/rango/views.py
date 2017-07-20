from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Lategory
from rango.models import Page
from rango.forms import LategoryForm
def index(request):
    # return HttpResponse("Rango says hey there world!<br/> <a href='/rango/about'>About</a>")
    #context_dict ={'boldmessage':'I am bold font from the context'}
    #return render(request,'rango/index.html',context_dict)
    category_list = Lategory.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {'categories':category_list}
    context_dict['pages'] = page_list
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

def add_category(request):
    if request.method == 'POST':
        form = LategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = LategoryForm()

    return render(request, 'rango/add_category.html', {'form':form})
from rango.forms import PageForm

def add_page(request, category_name_slug):

    try:
        cat =Lategory.objects.get(slug=category_name_slug)
    except Lategory.DoesNoExist:
        cat = None
    if request.method == 'POST':
        form = PageForm(request.POST)
        if form.is_valid():
            if cat:
                page = form.save(commit=False)
                page.category = cat
                page.views = 0
                page.save()

                return category(request, category_name_slug)
        else:
            print form.errors
    else:
        form = PageForm()

    context_dict = {'form':form, 'category':cat}
    return render(request, 'rango/add_page.html', context_dict)

from rango.forms import UserForm, UserProfileForm


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and userprofile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = userprofile_form.save(commit=False)
            profile.user = user

            if 'pictrue' in request.FILES:
                profile.save()

            registered = True

        else:
            print user_form.errors, userprofile_form.errors


    else:

        user_form = UserForm()

        userprofile_form = UserProfileForm()

    return render(request, 'rango/register.html',
                            {'user_form':user_form,
                            'userprofile_form':userprofile_form,
                            'registered':registered
                            }
                  )







