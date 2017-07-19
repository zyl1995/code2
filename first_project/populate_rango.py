import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

from rango.models import Lategory, Page

def populate():
    python_cat = add_cat(name='Python',views=987,likes=654)

    add_page(cat=python_cat,
             title="Official Python Tutorial",
             url="http://docs.python.org/2/tutorial/")

    add_page(cat=python_cat,
             title="How to Think like a Computer Scientist",
             url="http://www.greenteapress.com/thinkpython/")

    add_page(cat=python_cat,
             title="Learn Python in 10 Minutes",
             url="http://www.korokithakis.net/tutorials/python/")

    django_cat = add_cat("Django",views=98,likes=65)

    add_page(cat=django_cat,
             title="Official Django Tutorial",
             url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/")

    add_page(cat=django_cat,
             title="Django Rocks",
             url="http://www.djangorocks.com/")

    add_page(cat=django_cat,
             title="How to Tango with Django",
             url="http://www.tangowithdjango.com/")

    frame_cat = add_cat("Other Frameworks",views=7,likes=4)

    add_page(cat=frame_cat,
             title="Bottle",
             url="http://bottlepy.org/docs/dev/")

    add_page(cat=frame_cat,
             title="Flask",
             url="http://flask.pocoo.org")
    for c in Lategory.objects.all():
        for p in Page.objects.filter(category=c):
            print "-{0}-{1}".format(str(c), str(p))

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title, url=url, views=views)[0]
    return p

def add_cat(name,views,likes):
    c = Lategory.objects.get_or_create(name=name,views=views,likes=likes)[0]
    return c

if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()
