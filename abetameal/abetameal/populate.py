#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
populate

Description
- populates db with categries, meals and ingredients
- creates test User and Homes

Functions
- populate()
- create_meals()
- create_categories()
- create_homes()
- create_users()
"""

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'abetameal.settings')

import django, csv
django.setup()

import json
import urllib
import urllib2
from datetime import date

from meal.models import Ingredient
from meal.model_populate import ModelPopulate
from meal.models import Home, Preferance

# Setting up matrix and index items
from indexs.indexList import IndexList
from indexs.mealMatrix import MealMatrix

# Glodal vars to help populate database of meals
Num_of_meals = 51
mealIndex = IndexList()
ingrdIndex = IndexList()
meals = MealMatrix()
db = ModelPopulate()

DIR_PROJECT = ''
# DIR_PROJECT = 'abetameal/'

def populate():
  create_meals()
  h = create_homes()
  print 'populated homes: ', h, h[0].id, h[1].id, h[3].id

  u, u_h = create_users()
  print 'populated users: ', u, u_h.users, u_h

def create_meals():
  # populate database with meals and set up matrix
  with open( DIR_PROJECT + 'meal_ingredients.csv', 'rb') as csvfile:
      row = csv.reader(csvfile, delimiter=',')
      for ingr in row:
          if ingr[0] == 'ingredient':
              pass
          else:
              ingrdIndex.add_item(ingr[0])
              index_of_ingrd = ingrdIndex.get_index(ingr[0]) # stops plurals being added
              
              # check that ingredents plural version doesn't exist
              try:
                i = Ingredient.objects.get(index = index_of_ingrd)
                if i.name ==  ingrdIndex.get_item(index_of_ingrd) + 's':
                  i.name = ingrdIndex.get_item(index_of_ingrd)
                else:
                  db.add_ingredients(ingrdIndex.get_item(index_of_ingrd), index_of_ingrd )
              except Exception:
                db.add_ingredients(ingrdIndex.get_item(index_of_ingrd), index_of_ingrd )
                
  # create meal matrix
  meals.set_size(ingrdIndex.size(), Num_of_meals)
  
  # populate meal index, meal matrix and save all meals in database
  with open( DIR_PROJECT + 'meal_recipe.csv', 'rb') as csvfile:
   row = csv.reader(csvfile, delimiter=',')
   
   for meal in row:
       # add meal to index and store all data
       if meal[0] != 'meal name':
        mealIndex.add_item(meal[0])
        meal_in = mealIndex.get_index(meal[0])
       
        if meal[2] != 'ingredients':
         # split up the list if character is an alphanumeric character or on a only white space character
         meal_ingr = ''.join(''.join(meal[2].split('[')).split(']')).split(',')
         for i in range(0, len(meal_ingr)):
          meal_ingr[i] = meal_ingr[i].split("'") #''.join(meal_ingr[i].split("'"))
          meal_ingr[i][0] ='.'
          meal_ingr[i][2] ='.'
          meal_ingr[i] =''.join(''.join(meal_ingr[i]).split("."))
         
         for ingr in meal_ingr:
          # add ingredients to meal matrix
          if ingrdIndex.contains_item(ingr):
            index_of_ingrd = ingrdIndex.get_index(ingr)
            meals.add_ing(meal_in,index_of_ingrd)

            # count ingredients  
            i = Ingredient.objects.get(index = index_of_ingrd)
            num = i.amount
            i.amount = num + 1
            i.save()
            #print 'i.amount: ', i.amount, 'i.name', i.name
          
        meal_ingredients = meals.get_ingr(meal_in)
        meal_recipe = 'http://www.bbcgoodfood.com'+meal[3]
        #print 'To be added',meal[0], meal[1],meal_in, meal_recipe, meal_ingredients
        added_meal = db.add_meal(meal[0], meal[1],meal_in, meal_recipe, meal_ingredients)

def create_homes():
  # add 4 homes
  homes = []
  home_nos = [ x for x in range(1,5)]
  h_name = 'Home '
  for home in home_nos:
    homes.append( db.add_home(h_name + str(home)) )
  return homes

def create_users():
  # add passwords
  users_names = ['Joel','Kaz']
  users =[]
  for name in users_names:
    u = db.add_user(name,name+'@mail.com','password')
    h = Home.objects.get( name= 'Home 3')
    user = db.add_userprofile(u, h.id, [0], [1,2], 'M')
    users.append( user )
  db.update_home(h, [users[0].id, users[1].id] , 0 )
  return users, h


# Start execution here!
if __name__ == '__main__':
  print "Starting meal model test script..."
  populate()