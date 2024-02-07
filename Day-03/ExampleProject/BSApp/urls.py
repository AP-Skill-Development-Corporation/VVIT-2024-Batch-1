from django.urls import path
from BSApp import views

urlpatterns = [
	path('',views.home),
]