from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Lategory
from rango.models import Page
from rango.forms import LategoryForm

from datetime import  datetime


def index(request):
    # return HttpResponse("Rango says hey there world!<br/> <a href='/rango/about'>About</a>")
    #context_dict ={'boldmessage':'I am bold font from the context'}
    #return render(request,'rango/index.html',context_dict)
    #request.session.set_test_cookie()
    category_list = Lategory.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {'categories':category_list}
    context_dict['pages'] = page_list



    visits = request.session.get('visits')

    if not visits:
        visits = 1
    reset_last_visit_time = False

    last_visit = request.session.get('last_visit')

    if last_visit:
        last_visit_time = datetime.strptime(last_visit[:-7],"%Y-%m-%d %H:%M:%S")

        if (datetime.now() - last_visit_time).seconds > 5:

            visits = visits + 1

        reset_last_visit_time = True

    else:
        reset_last_visit_time = True

    if reset_last_visit_time:

        request.session['last_visit'] = str(datetime.now())

        request.session['visit'] = visits

    context_dict['visits'] = visits

    response = render(request,'rango/index.html',context_dict)

    return response




    # visits = int(request.COOKIES.get('visits','1'))
    #
    #
    #
    # reset_last_visit_time = False
    #
    #
    # response = render(request,'rango/index.html',context_dict)
    #
    # if 'last_visit' in request.COOKIES:
    #     last_visit = request.COOKIES['last_visit']
    #     #last_visit_time = datetime.strftime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")
    #     last_visit_time = datetime.strptime(last_visit[:-7], "%Y-%m-%d %H:%M:%S")
    #
    #     if (datetime.now() - last_visit_time).seconds > 5:
    #         visits = visits + 1
    #
    #         reset_last_visit_time = True
    # else:
    #     reset_last_visit_time = True
    #
    #     context_dict['visit'] = visits
    #
    #     response = render(request,'rango/index.html',context_dict)
    #
    # if reset_last_visit_time:
    #
    #     response.set_cookie('last_visit', datetime.now())
    #
    #     response.set_cookie('visits', visits)
    #
    # return  response

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
    #if request.session.test_cookie_worked():
    #    print ">>>>>Test COOKIE WORKED"
    #    request.session.delete_test_cookie()
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

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']


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

from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:

            if user.is_active:

                login(request, user)

                return HttpResponseRedirect('/rango/')

            else:
                return HttpResponse("Your Rango account is disabled.")

        else:
            print "Invalid login details:{0},{1}".format(username,password)
            return HttpResponse("Invalid login details supplied")

    else:
        return render(request,'rango/login.html',{})

from django.contrib.auth.decorators import login_required


@login_required
def restricted(request):
    return HttpResponse("Since you are logged in, you can see this text!")


from django.contrib.auth import  logout

@login_required
def user_logout(request):
    logout(request)

    return  HttpResponseRedirect('/rango/')

from rango.bing_search import run_query

def search(request):

    result_list = []

    if request.method == 'POST':
        query = request.POST['query'].strip()

        if query:
            # Run our Bing function to get the results list!
            result_list = run_query(query)

    return render(request, 'rango/search.html', {'result_list': result_list})



def track_url(request):

    if request.method == 'GET':
        if 'page_id' in request.GET:
            page_id = request.GET['page_id']




