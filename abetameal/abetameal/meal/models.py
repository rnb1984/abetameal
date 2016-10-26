from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField, JSONField
import os
from django.conf import settings
from django.core.validators import validate_email
from django.template.defaultfilters import slugify
from datetime import date

"""
- UserProfile
- Meal
- Ingredients
- PairPreferance
- Dinner
- Home
- Categories
- Preferance
"""

GENDER_CHOICES = (
    ('U', 'Undisclosed'),
    ('F', 'Female'),
    ('M', 'Male'), 
)

class UserProfile(models.Model):
    """
	UserProfile
	- Stores user details of participance
	to be used in post evaluation.
	"""
	
    user = models.OneToOneField(User)
    home = models.IntegerField(default=0)
    pref = models.IntegerField(default=0)
    dob = models.DateField(default=date.today())
    gender = models.CharField(default="U", max_length=1, choices=GENDER_CHOICES)
    allergies = ArrayField( models.IntegerField(),null=True, blank=True)
    diets = ArrayField( models.IntegerField(),null=True, blank=True)
    hunger = models.IntegerField(default=0)
    slug = models.SlugField(max_length=128)

    def save(self, *args, **kwargs):
         self.slug = slugify(self.user.username)
         super(UserProfile, self).save(*args, **kwargs)

    def __unicode__(self):
    	return self.user.username
        
class Meal(models.Model):
	"""
	Meal
	- Stores name of meal, pic of meal, index meal is on matrix of meal and a feature vecture of ingredients
	"""

	name = models.CharField(max_length=128) 
	index = models.IntegerField(default=0)
	pic = models.URLField( blank=True )
	recipe = models.URLField( blank=True )
	ingrs = ArrayField( models.IntegerField(), blank=True)
	cuisines = ArrayField( models.IntegerField(),null=True, blank=True)
	allergies = ArrayField( models.IntegerField(),null=True, blank=True)
	diets = ArrayField( models.IntegerField(),null=True, blank=True)
	data = JSONField(default={}, blank=True)
	slug = models.SlugField(max_length=128) # defaults to 50 on postgres
	
	def save(self, *args, **kwargs):
	    self.slug = slugify(self.name)
	    super(Meal, self).save(*args, **kwargs)
	
	def __unicode__(self):
	    return self.name

class Ingredient(models.Model):
	"""
	Ingredient
	- Stores name of ingredient and index of ingredients on meal matrix with the amount with total counted in meals
	"""
	
	name = models.CharField(max_length=128)
	index = models.IntegerField(default=0)
	amount = models.IntegerField(default=0)
	slug = models.SlugField(max_length=128)
	
	def save(self, *args, **kwargs):
	    self.slug = slugify(self.name)
	    super(Ingredient, self).save(*args, **kwargs)

	def __unicode__(self):
	    return self.name

class PairPreferance(models.Model):
	"""
	UserPreferance
	- Stores pair of meal index, with 0 or 1 rating, used in comparsisons
	"""
	user = models.IntegerField(default=0)
	index = models.IntegerField(default=0)
	pairsize = models.IntegerField(default=0)
	value = models.IntegerField(default=2)
	date = models.DateField(default=date.today())
	time = models.IntegerField(default=0)
	slug = models.SlugField(max_length=128)
	
	def save(self, *args, **kwargs):
	    self.slug = slugify(self.index)
	    super(PairPreferance, self).save(*args, **kwargs)
	
	def __unicode__(self):
		index = str(self.index)
		return index

class Dinner(models.Model):
	"""
	Dinner
	- Stores details on dinner meal and ranked meals
	"""
	
	name = models.CharField(max_length=128)
	users = ArrayField( models.IntegerField(), blank=True)
	home = models.IntegerField(default=0)
	meal = models.IntegerField(default=0)
	menu = JSONField(default={}, blank=True)
	pref = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)
	time = models.IntegerField(default=0)
	cooking = models.BooleanField(default=False)
	pickup = JSONField(default={}, blank=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	slug = models.SlugField(max_length=128)
	
	def save(self, *args, **kwargs):
	    self.slug = slugify(self.name)
	    super(Dinner, self).save(*args, **kwargs)

	def __unicode__(self):
	    return self.meal

class Home(models.Model):
	"""
	Home
	- Stores details of the home
	"""
	name = models.CharField(max_length=128)
	users = ArrayField( models.IntegerField(),null=True, blank=True)
	pref = models.IntegerField(default=0)
	slug = models.SlugField(max_length=128)
	
	def save(self, *args, **kwargs):
	    self.slug = slugify(self.name)
	    super(Home, self).save(*args, **kwargs)

	def __unicode__(self):
	    return self.name

class Categories(models.Model):
	"""
	Categories
	- Stores name of categry with items that make up the category
	"""
	
	name = models.CharField(max_length=128)
	items = JSONField(default={}, blank=True)
	slug = models.SlugField(max_length=128)
	
	def save(self, *args, **kwargs):
	    self.slug = slugify(self.name)
	    super(Categories, self).save(*args, **kwargs)

	def __unicode__(self):
	    return self.name

class Preferance(models.Model):
	"""
	Preferance
	- Stores meal pair index, with 0 or 1 rating, used in comparsisons
	- Stores latest prediction as meal index integer
	- Stores boolean for if prediction was true or false
	"""
	owner = models.IntegerField(default=0)
	ownertype = models.BooleanField(default=False)# set preferances to frue if user and false for home
	rank = ArrayField( models.IntegerField(), null=True, blank=True)
	model = JSONField(default={}, blank=True) # contains taining pairs
	pairs = JSONField(default={}, blank=True) # contains current set of pairs
	ready = models.BooleanField(default=False)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __unicode__(self):
		rank =str(self.owner)
		if self.rank:
			rank = rank+':'
			for r in self.rank:
				rank = rank+str(r)+','
		return rank