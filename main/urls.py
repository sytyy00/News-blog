from django.urls import path, re_path
from . import views
from django.views.generic import ListView, DetailView
from .models import Articles

urlpatterns = [

    re_path(r'^$', views.articles),
    # re_path(r'^(?P<article_id>\d+)$',views.article),
    re_path(r'^news(?P<article_id>\d+)$', views.article),

]
