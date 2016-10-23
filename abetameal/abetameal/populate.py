#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'abetameal.settings')

import django, csv
django.setup()

import json
import urllib
import urllib2
from datetime import date

#from meal.models import Meal, Ingredient, UserProfile
from meal.models import Ingredient
from meal.model_populate import ModelPopulate

# classes to set up matrix and index items
from indexs.indexList import IndexList
from indexs.mealMatrix import MealMatrix

# Glodal vars to help populate database of meals
Num_of_meals = 51
mealIndex = IndexList()
ingrdIndex = IndexList()
meals = MealMatrix()
db = ModelPopulate()

DIR_PROJECT = 'abetameal/'

def populate():
  
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
  with open(DIR_PROJECT + 'meal_recipe.csv', 'rb') as csvfile:
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

# Start execution here!
if __name__ == '__main__':
  print "Starting meal face model test script..."
  populate()