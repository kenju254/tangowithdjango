import os

def populate():
    python_cat = add_cat("Python")
    python_views = 128
    python_likes = 64

    add_page(cat=python_cat,
             title="Official Python Tutorial",
             url="http://docs.python.org/2/tutorial/",
             views=python_views,
             likes=python_likes)

    add_page(cat=python_cat,
             title="How To Think like a Computer Scientist",
             url="http://www.greenteapress.com/thinkpython/",
             views=python_views,
             likes=python_likes)

    add_page(cat=python_cat,
             title="Learn Python in 10 Minutes",
             url="http://www.korokithakis.net/tutorials/python/",
             views=python_views,
             likes=python_likes)


    django_cat = add_cat("Django")
    django_views = 64
    django_likes = 32

    add_page(cat=django_cat,
             title="Official Django Tutorial",
             url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/",
             views=django_views,
             likes=django_likes)

    add_page(cat=django_cat,
             title="Django Rocks",
             url="http://www.djangorocks.com/",
             views=django_views,
             likes=django_likes)


    add_page(cat=django_cat,
             title="How to Tango with Django",
             url="http://www.tangowithdjango.com/",
             views=django_views,
             likes=django_likes)


    frame_cat = add_cat("Other Frameworks")
    frame_views = 32
    frame_likes = 16

    add_page(cat=frame_cat,
             title="Bottle",
             url="http://bottlepy.org/docs/dev/",
             views=frame_views,
             likes=frame_likes)


    add_page(cat=frame_cat,
             title="Flask",
             url="http://flask.pocoo.org",
             views=frame_views,
             likes=frame_likes)

    #Printing out to the user
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print " - {0} - {1}".format(str(c), str(p))

def add_page(cat, title, url, views=0 , likes=0):
    p = Page.objects.get_or_create(category=cat, title=title, url=url,
        views=views, likes=likes )[0]
    return p

def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    return c

#Start Executing the script

if __name__ == '__main__':
    print "Starting Rango population script ..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')
    from rango.models import Category, Page
    populate()


