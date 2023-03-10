"""first_django_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from first_django_site import view 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users', view.get_all_users ), #get all users
    path('api/user/<int:id>', view.get_single_user ), #get single user by id
    path('api/create', view.create_user ), #create user
    path('api/update/<int:id>', view.update_user ), #update user with complete user data
    path('api/patch-update/<int:id>', view.partial_update_user ), #patch update user data
    path('api/delete/<int:id>', view.delete_user) # delete user
]
