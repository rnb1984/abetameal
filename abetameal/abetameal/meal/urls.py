from django.conf.urls import url
from meal import views


urlpatterns = [
    # url patterns for meal app
    #url(r'^$', views.index, name='index'),
    url(r'^pairs/first/$', views.comparision_pair_first, name='first-comp-pairs'),
    url(r'^pairs/$', views.comparision_pair, name='comp-pairs'),
    
]