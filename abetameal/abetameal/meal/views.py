from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from meal.models import Meal, Ingredient, UserProfile, PairPreferance
import csv

# For the RESTFUL API
from rest_framework import generics
from meal.serializers import MealSerializer, IngredientSerializer, UserProfileSerializer, PairPreferanceSerializer


# Landing page
def index(request):
    meals = Meal.objects.all().order_by('index')
    ingredients = Ingredient.objects.all().order_by('index')

    context_dict = { 'title' : 'Welcome','meals' : meals, 'ingredients':ingredients }
    return render(request, 'meal/index.html', context_dict)

# Register
# Login page
# Log Out
# Restrictions

"""
REST APIs
- Meal
-- Meal List
- Ingredient
-- Ingredient List
- User
-- UserProfile List
-- UserProfile Details
- Pairs
-- PairPref Lists
-- PairPref Details
"""
# Meals
class MealList(generics.ListCreateAPIView):
    # returns a list of Meals
    queryset = Meal.objects.all().order_by('index')
    serializer_class = MealSerializer

class MealDetails(generics.RetrieveUpdateDestroyAPIView):
    # edit a Meal on id/pk
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

# Ingredients
class IngredientList(generics.ListCreateAPIView):
    # edit a ingredients on id/pk
    queryset = Ingredient.objects.all().order_by('index')
    serializer_class = IngredientSerializer

class IngredientDetails(generics.RetrieveUpdateDestroyAPIView):
    # returns a list of ingredients
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

   
class UserProfileList(generics.ListCreateAPIView):
    # returns a list of profiles
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    
class UserProfileDetails(generics.RetrieveUpdateDestroyAPIView):
    # edit a profile depending on a id/pk
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    
class PairPrefLists(generics.ListCreateAPIView):
    # returns a list of pairs
    queryset = PairPreferance.objects.all()
    serializer_class = PairPreferanceSerializer

class PairPrefDetails(generics.RetrieveUpdateDestroyAPIView):
    # edit a pairs depending on a id/pk
    queryset = PairPreferance.objects.all()
    serializer_class = PairPreferanceSerializer    