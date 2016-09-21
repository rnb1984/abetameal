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
- Meal
- Ingredients
- UserProfile
- UserPreferance
"""

GENDER_CHOICES = (
    ('U', 'Undisclosed'),
    ('F', 'Female'),
    ('M', 'Male'), 
)

# REDEFINE MODEL !!!
class UserProfile(models.Model):
    """
	UserProfile
	- Stores user details of participance
	to be used in post evaluation.
	"""
	
    user = models.OneToOneField(User)
    exp_index = models.IntegerField(default=0)
    dob = models.IntegerField(default=0)
    gender = models.CharField(default="U", max_length=1, choices=GENDER_CHOICES)
    allergies = models.CharField(default="0", max_length=128)
    diet = models.CharField(default="0", max_length=128)
    occupation = models.IntegerField(default=0)
    nationality = models.CharField(default="0", max_length=128)
    
    
    """
	UserPreferance
	- Stores fk to meal pair index, with 0 or 1 rating, used in comparsisons
	- Stores latest prediction as meal index integer
	- Stores boolean for if prediction was true or false
	"""
	
	# Current prediction = int    predict = models.IntegerField(default=0)			!!
	# Prediction correct = boolean   correct = models.BooleanField(default=False)	!!
    slug = models.SlugField()

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
	pic = models.URLField()
	recipe = models.URLField()
	ingrs = ArrayField(models.IntegerField(), blank=True)
	# Array specific to Postgres
	# allergies = ArrayField(models.CharField(max_length=128, default=''), blank=True), ~ possible feature for end system
	# diet = ArrayField(models.CharField(max_length=128, default=''), blank=True), ~ possible feature for end system
	data = JSONField(default={})
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
	slug = models.SlugField()
	
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
	user = models.IntegerField(default=0)# Index of pair
	index = models.IntegerField(default=0)# Value of pair
	value = models.IntegerField(default=2)
	date = models.DateField(default=date.today())# Date of pair made
	time = models.IntegerField(default=0)
	slug = models.SlugField()
	
	def save(self, *args, **kwargs):
	    self.slug = slugify(self.index)
	    super(PairPreferance, self).save(*args, **kwargs)
	
	def __unicode__(self):
		index = str(self.index)
		return index