from rest_framework import serializers
from meal.models import Meal, Ingredient, UserProfile, PairPreferance

"""
Serializers
Create api's for the models in a similiar way forms are used
"""

class MealSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meal
        fields = "__all__"


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = "__all__"


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id','dob','gender','allergies','diet', 'occupation', 'nationality')


class PairPreferanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = PairPreferance
        fields = ( 'id','index','value', 'time')