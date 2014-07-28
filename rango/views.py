# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

from rango.models import Category, Page
from rango.forms import CategoryForm , PageForm , UserForm, UserProfileForm


def encode_url(str):
    return str.replace('','_')

def decode_url(str):
    return str.replace('_', '')

def register(request):
    context = RequestContext(request)

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)

            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()

            registered = True
        else:
            print user_form.errors , profile_form.errors

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

def index(request):
    #We are requesting the context of the request.
    #This context contains information such as the client's machine details and metadata
    context = RequestContext(request)

    #What we do is we construct a dictionary to pass to the template engine as its context
    #Note the key boldmessage is the same as {{ boldmessage }} in the template!

    category_list = Category.objects.order_by('likes')[:5]
    context_dict = {'categories' : category_list}

    #Return a rendered response to send to the client.
    #We make use of the shortcut function to make our lives easier.
    #Note that the first parameter is the template we wish to use.
    return render_to_response('rango/index.html', context_dict, context)



def category(request, category_name_url):

    context = RequestContext(request)

    category_name = decode_url(category_name_url)

    context_dict = {'category_name' : category_name,
                    'category_name_url': category_name_url}

    category_list = Category.objects.order_by('likes')[:5]
    context_dict = {'categories': category_list}

    try:
        category = Category.objects.get(name__iexact=category_name)
        context_dict['category'] = category

        pages = Page.objects.filter(category=category).order_by('views')

        context_dict['pages'] = pages

    except Category.DoesNotExist:
        pass

    return render_to_response('rango/category.html', context_dict, context)

def add_category(request):

    context = RequestContext(request)

    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return index(request)

        else:
            print form.errors

    else:
        form = CategoryForm()

    return render_to_response('rango/add_category.html', {'form': form}, context)

def add_page(request, category_name_url):
    context = RequestContext(request)

    category_name = decode_url(category_name_url)
    if request.method == "POST":
        form = PageForm(request.POST)

        if form.is_valid():
            form.save(commit=False)

            try:
                cat = Category.objects.get(name=category_name)
                page.create = cat
            except Category.DoesNotExist:
                return render_to_response('rango/add_category.html', {}, context)

            page.views = 0

            page.save()

            return category(request, category_name_url)

        else:
            print form.errors

    else:
        form = PageForm()

    return render_to_response('rango/add_page.html',
        {'category_name_url': category_name_url,
        'category_name':category_name,'form':form},
        context)






def about(request):
    return render_to_response('rango/about.html')
