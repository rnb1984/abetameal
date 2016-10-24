from django.contrib import admin
from meal.models import Meal, Ingredient, UserProfile, PairPreferance, Dinner, Home, Categories,Preferance

# Register your models here.
admin.site.register(Meal)
admin.site.register(Ingredient)
admin.site.register(UserProfile)
admin.site.register(PairPreferance)
admin.site.register(Dinner)
admin.site.register(Home)
admin.site.register(Categories)
admin.site.register(Preferance)