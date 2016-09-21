"""abetameal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.views.static import *

# For API's
from meal import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    
    # APIs
    url(r'^meals/', views.MealList.as_view(), name='meals'),
    url(r'^meal/(?P<pk>[0-9]+)/$', views.MealDetails.as_view(), name='meal'),
    url(r'^ingredients/', views.IngredientList.as_view(), name='ingredients'),
    url(r'^ingredient/(?P<pk>[0-9]+)/$', views.IngredientDetails.as_view(), name='ingredient'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # For uploading media files

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)