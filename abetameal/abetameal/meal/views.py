from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from meal.model_populate import ModelPopulate
from meal.models import Meal, Ingredient, UserProfile, Home, Preferance, Dinner
import csv

# Comparision Pairs
from pairSet.pairs import PairSet

# Landing page
def index(request):
    meals = Meal.objects.all().order_by('index')
    ingredients = Ingredient.objects.all().order_by('index')

    context_dict = { 'title' : 'Welcome','meals' : meals, 'ingredients':ingredients }
    return render(request, 'meal/index.html', context_dict)

# Register page !! Update page direct !!
def register(request):
    # Reister for data gathering
    context_dict={}
    # A boolean value for telling the template whether the registration was successful
    registering = True

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':

        user_form = UserForm(data=request.POST)
        # valid forms only
        if user_form.is_valid():

            # Save the user's form data to database.
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            # create user profile object with userprofile details and user id
            profile = UserProfile.objects.get_or_create(user=user)[0] # add to pref pairs
            profile.exp_index = get_user_index()
            profile.save()
            
            # feed back
            context_dict = {'form': registering, 'id': profile.id}
            return HttpResponseRedirect('/login/')

        # Invalid form or forms - mistakes or something else?
        else:
            return render(request, 'pizza_ml/user/register.html',{'user_form': user_form, 'errors': user_form.errors})

    # For get request send user form
    else:
        user_form = UserForm()
        context_dict ={ 'title' : 'Register' ,'user_form': user_form, 'registering': registering}
    
    return render(request, 'pizza_ml/user/register.html', context_dict)

# Login page !! Update page direct !!
def user_login(request):

    if request.method == 'POST':
        
        username = request.POST.get('username')
        password = request.POST.get('password')

        # use username/password to find User object
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                # If the account is valid or already login, go back to home page
                login(request, user)
                return HttpResponseRedirect('/details/')
            else:
                # Not logged in
                return HttpResponse("Your are not logged in.")
        else:
            # No user found
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    else:
        # not logged in so register
        return render(request, 'pizza_ml/user/login.html', {'title' : 'Login'})

# Log out !! Update page direct !!
@login_required
def user_logout(request):
    # Uses django defaults to log out 
    logout(request)
    return HttpResponseRedirect('/pizzaface/')

# Restrictions
@login_required
def restricted(request):
    return HttpResponse("You are not logged in")

"""
Views
- Preferance Page
- Details Page
- Home Feed
- Meal
"""
def preferances(request):
    context_dict = { 'title' : 'Preferance Page' }
    return render(request, 'meal/index.html', context_dict)

def details(request):
    context_dict = { 'title' : 'Details Page' }
    return render(request, 'meal/index.html', context_dict)

def home_feed(request):
    context_dict = { 'title' : 'Home' }
    return render(request, 'meal/index.html', context_dict)

def dinner_meal(request):
    context_dict = { 'title' : 'Dinner' }
    return render(request, 'meal/index.html', context_dict)


"""
Views API
- comparision_pairs
"""
def comparision_pair_first(request):
    # Updates a single pair but will get a set
    user= request.user
    if request.method == 'GET':
        # API to Create pairs set
        context_dict =  get_first_comparision_pairs()
        return JsonResponse(context_dict)

def comparision_pair(request):
    # Updates a single pair but will get a set
    #user= request.user
    user = User.objects.get(username='Joel')
    if request.method == 'GET':
        # API to Create pairs set
        context_dict =  get_comparision_pairs(user.id)
        return JsonResponse(context_dict)

    elif request.method == 'POST':
        # API to Update pairs
        json_dict = json.loads(request.body)
        index =  json_dict['index']
        value =  json_dict['value']
        context_dict = update_compared_pair(user.id, index, value)
        return JsonResponse(context_dict)

    elif request.method == 'PUT':
        # API to Add pairs
        json_dict = json.loads(request.body)
        index =  json_dict['index']
        value =  json_dict['value']
        context_dict = add_compared_pair(user.id, index, value)
        return JsonResponse(context_dict)

"""
Helpers for Views
- add_compared_pair
- update_compared_pair
- get_comparision_pairs

""" 
def add_compared_pair(userid, index, value):
    # Add new pair value
    pref = Preferance.objects.get(owner=userid, ownertype=True)
    pref.model['train'][0]['index'].append(index)
    pref.model['train'][0]['value'].append(value)
    pref.save()
    return pref

def update_compared_pair(userid, index, value):
    print 'pairs vars: ',userid, index, value
    # Updates pair value
    pref = Preferance.objects.get(owner=userid, ownertype=True)
    end = len(pref.model['train'][0]['index'])
    for i in range (0, end):
        if index == pref.model['train'][0]['index'][i]:
            pref.model['train'][0]['index'].pop(i)
            pref.model['train'][0]['value'].pop(i)
            pref.model['train'][0]['index'].append(index)
            pref.model['train'][0]['value'].append(value)
            pref.save()
            return pref
    return add_compared_pair(userid, index, value)

def get_comparision_pairs(user):
    pairSet = PairSet()
    # create new comparision pair set based last pair in the models train indexs
    pref = Preferance.objects.get(owner=user, ownertype=True)
    start = pref.model['train'][0]['index'][-1]
    comparision_pairs = pairSet.get_dict(start)
    return comparision_pairs

def get_first_comparision_pairs():
    pairSet = PairSet()
    # create first comparision pair 
    comparision_pairs = pairSet.get_first_dict()
    return comparision_pairs