from django.contrib import admin
from meal.models import Meal, Ingredient, UserProfile, PairPreferance

# Register your models here.
admin.site.register(Meal)
admin.site.register(Ingredient)
admin.site.register(UserProfile)
admin.site.register(PairPreferance)