"""src URL Configuration

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
from django.urls    import path

from src.controllers.user import UserController
from src.controllers.class_ import ClassController
from src.controllers.instructor import InstructorController
from src.controllers.offer import OfferController
from src.controllers.proposal import ProposalController


urlpatterns = [
    path('api/login', 		UserController().login),
    path('api/check-username', UserController().check_username),
    path('api/register',  	UserController().register),
    path('api/instructors',  	InstructorController().get_instructors),
    path('api/my-classes',  	ClassController().get_classes),
    path('api/proposals',  	ProposalController().get_proposals),
    
    path('api/class/register',  ClassController().register),
    path('api/user/update',  UserController().update),
]
