# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 17:03:56 2023

@author: claud
"""

#from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name="home"),
]