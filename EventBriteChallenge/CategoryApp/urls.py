from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
#from CategoryApp.models import Category
from CategoryApp.challenge import Challenge

urlpatterns = patterns('',
						url(r'^$', ListView.as_view(
								queryset=Challenge.event,
								template_name="index.html")),
						)