from meal.models import Meal, Ingredient, UserProfile, Home, Preferance
from django.contrib.auth.models import User

"""
Model Populate
These are app specific model helper functions to add new objects to model
- Meal
- add_ingredients
- add_userprofile
- add_meal
"""
class ModelPopulate():
	def __init__(self):
		self.data=[]
	# Meal
	def add_meal(self, meal_name, meal_image, meal_index, meal_recipe, meal_ingredients): # populate database with meals
	  print "Meal added to database, meal_name", meal_name, "meal_image", meal_image, "meal_index_number", meal_index
	  empty = [0]
	  p = Meal.objects.get_or_create(name=meal_name.lower(),
	  	pic=meal_image,
	  	index=meal_index,
	  	recipe= meal_recipe,
	  	ingrs=meal_ingredients,
	  	cuisines= empty,
	  	allergies= empty,
	  	diets= empty )[0]
	  p.save()
	  return p

	# Ingredients
	def add_ingredients(self,ingr_name, ingr_index):  # saves ingredients to database
	  i = Ingredient.objects.get_or_create(name=ingr_name.lower(),index=ingr_index)[0]
	  i.save()
	  return i
	 
	# UserProfile
	def add_userprofile(self, user, home, allergies, diets, gender):
	  # Creates user profile and preferances objects for passed user
	  p = self.add_preferances(user.id, [0], True)# set preferances to false if users
	  u = UserProfile.objects.get_or_create(user= user, home=home, pref=p.id, gender=gender, allergies=allergies, diets=diets)[0]
	  u.save()
	  return u

	# User
	def add_user(self, username,email,password):
	    u = User.objects.create_user(username, email, password)
	    u.save()
	    return u

	# Home
	def add_home(self, h_name):
		print '-----**----', h_name
		h = Home.objects.create(name=h_name)
		h.save()
		p = self.add_preferances(h.id, [0], False)# set preferances to false if home
		h = self.update_home( h, [0], p.id )
		return h

	def update_home(self, h, users, pref ):
		# Home update with list of users and preferances
		if users[0] != 0:
			h.users = users
		if pref != 0:
			h.pref = pref
		h.save()
		return h

	# Preferances
	def add_preferances(self, owner, rank, owner_type):
	    p = Preferance.objects.create(owner=owner, rank=rank, ownertype=owner_type, pairs={
	    	'index': [0],
	    	},
	    	model={ 'train' : [{
	    	'index': [0],
	    	'value':[2],
	    	}],

	    	})
	    p.save()
	    print '----', owner, p
	    return p