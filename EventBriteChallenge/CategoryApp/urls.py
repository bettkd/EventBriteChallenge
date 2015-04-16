from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from CategoryApp.models import Category

urlpatterns = patterns('',
						url(r'^$', ListView.as_view(
								queryset=Category.objects.all().order_by("-date")[:10],
								template_name="index.html")),
						)