"""RestApiDemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from rest_api import views
urlpatterns = [
    path('create_car/', views.CreateCarView.as_view(), name='create_car'),
    path('create_car_type/', views.CreateCarTypeView.as_view(), name='create_car_type'),
    path('admin/', admin.site.urls),


    path('', views.ShowAllView.as_view()),
    path('get_car_by_type/', views.get_cars_by_type, name='get_car_by_type'),
    # path('show_me_get/', views.show_me_get),
    # path('tabelka/', views.multiple),
]

