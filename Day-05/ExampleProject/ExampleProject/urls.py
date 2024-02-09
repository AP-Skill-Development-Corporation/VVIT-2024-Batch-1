"""ExampleProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from VVITApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('g/',views.demo),
    path('k/<str:n>/',views.greet),
    path('gh/<str:a>/<int:b>/',views.stdnt),
    path('eh/',views.ky),
    path('my/<str:n>/',views.my),
    path('p/<str:en>/<int:es>/',views.emp),
    path('y/',views.ry),
    path('mg/<str:m>/',views.mg),
    path('stdt/<str:sname>/<str:branch>/<int:year>/<str:rollNo>/', views.student),
    path('ty/',views.np),
    path('ny/<str:a>/',views.fun),
    path('tm/<str:a>/<int:s>/<str:c>/<str:d>/',views.display),
    path('hn/',views.dr),
    path('',include('BSApp.urls')),
]
