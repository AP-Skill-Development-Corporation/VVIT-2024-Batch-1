from django.urls import path
from DemoApp import views

urlpatterns = [
	path('',views.home,name="hm"),
	path('reg/',views.usregister,name="ug"),
]