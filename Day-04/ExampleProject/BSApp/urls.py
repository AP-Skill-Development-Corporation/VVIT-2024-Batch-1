from django.urls import path
from BSApp import views

urlpatterns = [
	path('',views.home,name="hme"),
	path('abt/',views.about,name="ab"),
	path('std/',views.stdnt,name="st"),
	path('sp/<int:k>/',views.stdup,name="stpd"),
	path('sd/<int:m>/',views.stdlt,name="stdt"),
	path('empl/',views.emp,name="em"),
]