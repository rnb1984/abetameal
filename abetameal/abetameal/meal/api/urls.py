from django.conf.urls import url
#from rest_framework.urlpatterns import format_suffix_patterns
from .views import ( 
	MealList,
	MealDetails,
	IngredientList,
	IngredientDetails,
	UserProfileList,
	UserProfileDetails,
	PairPrefLists,
	PairPrefDetails,
	UserProfileList,
	UserProfileDetails,
	UserHomeDetails,
	PairPrefLists,
	PairPrefDetails,
	DinnerHomeDetails,
	DinnerMealDetails,
	)


urlpatterns = [
    # Orginal

    # url api patterns for meal app
    #url(r'^meals/create/$', views.index, name='create'),
    url(r'^meals/(?P<pk>\d+)/$', MealDetails.as_view(), name='meal-detail'),
    url(r'^meals/(?P<slug>[\w-]+)/$', MealDetails.as_view(), name='meal-details'),
    url(r'^meals/(?P<slug>[\w-]+)/edit/$', MealDetails.as_view(), name='meal-update'),
    url(r'^meals/(?P<slug>[\w-]+)/delete/$', MealDetails.as_view(), name='meal-deletes'),
    url(r'^meals/', MealList.as_view(), name='meals'),

    #url(r'^ingredients/create/$', views.index, name='create'),
    url(r'^ingredients/(?P<pk>[0-9]+)/$', IngredientDetails.as_view(), name='ingrd-detail'),
    url(r'^ingredients/(?P<slug>[\w-]+)/$', IngredientDetails.as_view(), name='ingrd-details'),
    url(r'^ingredients/(?P<slug>[\w-]+)/edit/$', IngredientDetails.as_view(), name='ingrd-update'),
    url(r'^ingredients/(?P<slug>[\w-]+)/delete/$', IngredientDetails.as_view(), name='ingrd-deletes'),
    url(r'^ingredients/', IngredientList.as_view(), name='ingredients'), 
]

#urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])