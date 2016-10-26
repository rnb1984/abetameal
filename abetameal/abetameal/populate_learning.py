#!/usr/bin/python
# -*- coding: utf-8 -*

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'abetameal.settings')

"""
populate_learnng
- create pairs to send to user
"""

import django, csv
django.setup()

import json

from pairSet.pairs import PairSet
from meal.model_populate import ModelPopulate
from meal.models import Meal, Ingredient, UserProfile, Home, Preferance

# Setting up matrix and index items
from indexs.indexList import IndexList
from indexs.mealMatrix import MealMatrix

# Glodal vars to help populate database of meals
Num_of_meals = 50
db = ModelPopulate()

def populate():
	# user
	users, home = create_users_homes()
	print users, home

	# create first learning pairs
	pairSet = PairSet()
	comp_pairs = pairSet.get_first_dict()
	print 'comp_pairs: ', comp_pairs

	# add values to pairs
	for index in comp_pairs['indexs']:
		add_compared_pair(users[0].id,index, 1)
	pref = Preferance.objects.get(owner=users[0].id, ownertype=True)
	print 'First indexs:', pref.model['train'][0]['index'], 'values:', pref.model['train'][0]['value']

	# set new pairs
	new_pairs = get_comparision_pairs(users[0].id)

	# update  more learning pairs
	for i in range(2, len(new_pairs['indexs'])):
		print i, new_pairs['indexs'][i]
		update_compared_pair(users[0].id, new_pairs['indexs'][i], 2)

	# update existinf pairs
	for i in range(2, len(comp_pairs['indexs'])):
		print i, comp_pairs['indexs'][i]
		update_compared_pair(users[0].id, comp_pairs['indexs'][i], 0)

	pref = Preferance.objects.get(owner=users[0].id, ownertype=True)
	print users[0],'Updated indexs:', pref.model['train'][0]['index'], 'values:', pref.model['train'][0]['value']

# Helpers for Views
# API to Add pairs
def add_compared_pair(userid, index, value):
    # Add new pair value
    pref = Preferance.objects.get(owner=userid, ownertype=True)
    pref.model['train'][0]['index'].append(index)
    pref.model['train'][0]['value'].append(value)
    pref.save()
    return pref

# API to Update pairs
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

# API to Create pairs set
def get_comparision_pairs(user):
    pairSet = PairSet()
    # create new comparision pair set based last pair in the models train indexs
    pref = Preferance.objects.get(owner=user, ownertype=True)
    start = pref.model['train'][0]['index'][-1]
    comparision_pairs = pairSet.get_dict(start)
    return comparision_pairs

def create_users_homes():
  # add passwords
  users_names = ['Tailor','Kimmy']
  users =[]
  for name in users_names:
    u = db.add_user(name,name+'@mail.com','password')
    h = Home.objects.get( name= 'Home 2')
    user = db.add_userprofile(u, h.id, [0], [1,2], 'F')
    users.append( user )
  db.update_home(h, [users[0].id, users[1].id] , 0 )
  return users, h

# Start execution here!
if __name__ == '__main__':
  print "Starting meal comparision pairs test script..."
  populate()