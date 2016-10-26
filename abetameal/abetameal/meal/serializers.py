from rest_framework.serializers import ModelSerializer, HyperlinkedIdentityField
from meal.models import Meal, Ingredient, UserProfile, PairPreferance, Dinner

"""
Serializers
Create api's for the models in a similiar way forms are used
- MealSerializer
- IngredientSerializer
- UserProfileSerializer
- PairPreferanceSerializer
- DinnerMealSerializer
- DinnerHomeSerializer
- UserHomeSerializer
"""

meal_url = HyperlinkedIdentityField(
        view_name='meal-api:meal-detail',
        lookup_field='pk',
        )
ingr_url = HyperlinkedIdentityField(
        view_name='meal-api:ingrd-detail',
        lookup_field='pk',
        )

class MealSerializer( ModelSerializer):
    url = meal_url
    class Meta:
        model = Meal
        fields = ["name","pic", "url","recipe", "ingrs", "slug"]

class MealDetailSerializer( ModelSerializer):

    class Meta:
        model = Meal
        fields = "__all__"

# Ingredient
class IngredientSerializer( ModelSerializer):
    url = ingr_url

    class Meta:
        model = Ingredient
        fields = ["name", "url"]

class IngredientDetailSerializer( ModelSerializer):
    
    class Meta:
        model = Ingredient
        fields = "__all__"

# UserProfile
class UserProfileSerializer( ModelSerializer):
    class Meta:
        model = UserProfile
        #fields = ('id','dob','gender','allergies','diet', 'occupation', 'nationality')
        fields = "__all__"

class PairPreferanceSerializer( ModelSerializer):
    class Meta:
        model = PairPreferance
        fields = ( 'id','index','value', 'time')

# Dinner
class DinnerMealSerializer( ModelSerializer):
    class Meta:
        model = Dinner
        fields = ( 'id','time','likes', 'cooking', 'menu', 'pickup')

class DinnerHomeSerializer( ModelSerializer):
    class Meta:
        model = Dinner
        fields = ( 'id','time','likes', 'cooking', 'meal', 'pickup')

# Home
class UserHomeSerializer( ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ( 'id','hunger')