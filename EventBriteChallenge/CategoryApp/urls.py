#from django.conf.urls import *
#from django.views.generic import ListView, DetailView
#from CategoryApp.models import Category
#import views

#urlpatterns = patterns('',
#						url(r'^$', ListView.as_view(
#								queryset=Challenge.event,
#								template_name="index.html")),
#						)

#urlpatterns = patterns('',
#		(r'^CategoryApp/$', 'views.hello_world'),
#)


from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.category,),
]