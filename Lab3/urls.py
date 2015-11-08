#-*- coding: UTF-8 -*- 。
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from library.views import *

urlpatterns = patterns('',
    # Examples:
    url(r'^add_author/$','library.views.add_author'),
    url(r'^add_book/$','library.views.add_book'),
    url(r'^book_view/$','library.views.book_view'),
    url(r'^delete/','library.views.delete'),
    url(r'^update/','library.views.update'),
    url(r'^search_form/$','library.views.search_form'),
    url(r'^$','library.views.search_form'),
    url(r'^search/$','library.views.search'),
)
