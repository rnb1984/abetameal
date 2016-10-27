from meal.models import (
	Meal,
	Ingredient,
	UserProfile,
	Home,
	PairPreferance,
	Preferance,
	Dinner,
	)

# For the RESTFUL API
from rest_framework.generics import (
	ListCreateAPIView,
	RetrieveAPIView,
	RetrieveUpdateDestroyAPIView,
	RetrieveUpdateAPIView,
	)
from meal.serializers import (
	MealSerializer,
	MealDetailSerializer,
	IngredientSerializer,
	IngredientDetailSerializer,
	UserProfileSerializer,
	PairPreferanceSerializer,
	DinnerMealSerializer,
	DinnerHomeSerializer,
	UserHomeSerializer
	)

"""
REST APIs
- Meal
-- Meal List
-- MealDetails
- Ingredient
-- Ingredient List
-- IngredientDetails
- User
-- UserProfile List
-- UserProfile Details
- Pairs
-- PairPref Lists
-- PairPref Details
- UserProfile
-- UserProfileList
-- UserProfileDetails
-- UserHomeDetails
- PairPref
-- PairPrefLists
-- PairPrefDetails
- Dinner
-- DinnerHomeDetails
-- DinnerMealDetails
"""
################################################################
# Meals
class MealList(ListCreateAPIView):
    # returns a list of Meals
    queryset = Meal.objects.all().order_by('index')
    serializer_class = MealSerializer

class MealDetails(RetrieveUpdateDestroyAPIView):
    # edit a Meal on id/pk
    queryset = Meal.objects.all()
    serializer_class = MealDetailSerializer
    lookup_field = 'pk'
################################################################
# Ingredients
class IngredientList(ListCreateAPIView):
    # edit a ingredients on id/pk
    queryset = Ingredient.objects.all().order_by('index')
    serializer_class = IngredientSerializer

class IngredientDetails(RetrieveUpdateDestroyAPIView):
    # returns a list of ingredients
    queryset = Ingredient.objects.all()
    serializer_class = IngredientDetailSerializer

################################################################
# UserProfile
class UserProfileList(ListCreateAPIView):
    # returns a list of profiles
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    
class UserProfileDetails(RetrieveUpdateDestroyAPIView):
    # edit a profile depending on a id/pk
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

################################################################
# Home
class UserHomeList(ListCreateAPIView):
    # edit a pairs depending on a id/pk
    queryset = UserProfile.objects.all()
    serializer_class =  UserHomeSerializer

class UserHomeDetails(RetrieveUpdateDestroyAPIView):
    # edit a pairs depending on a id/pk
    queryset = UserProfile.objects.all()
    serializer_class =  UserHomeSerializer

################################################################
# PairPref
class PairPrefLists(ListCreateAPIView):
    # returns a list of pairs
    queryset = PairPreferance.objects.all()
    serializer_class = PairPreferanceSerializer

class PairPrefDetails(RetrieveUpdateDestroyAPIView):
    # edit a pairs depending on a id/pk
    queryset = PairPreferance.objects.all()
    serializer_class = PairPreferanceSerializer

################################################################
# Dinner
class DinnerMealList(ListCreateAPIView):
    # edit a pairs depending on a id/pk
    queryset = Dinner.objects.all()
    serializer_class = DinnerMealSerializer

class DinnerMealDetails(RetrieveUpdateDestroyAPIView):
    # edit a pairs depending on a id/pk
    queryset = Dinner.objects.all()
    serializer_class = DinnerMealSerializer

class DinnerHomeDetails(RetrieveUpdateDestroyAPIView):
    # edit a pairs depending on a id/pk
    queryset = Dinner.objects.all()
    serializer_class = DinnerHomeSerializer
    # lookup_field = 'slug' # change url to <slug>
    # lookup_url_kwarg = 'abc' # change url to <abc>
    # def get_queryset(self, *args, **kwargs):
    # queryset_list = Dinner.objects.all()
    # query = self.request.GET.get('')
