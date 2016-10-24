from meal.models import Meal, Ingredient, UserProfile

"""
Model Populate
These are app specific model helper functions to add new objects to model
- Meal
- Ingredients
- UserProfile
- PairPreferances
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
	def add_userprofile(self, user):
	  u = UserProfile.objects.get_or_create(user= user)[0]
	  u.save()
	  return u

	# Preferances