"""
URL configuration for tripza project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from .import views

urlpatterns = [
    path('userview',views.user_view),
    path('add_package', views.addpackage,name="add_package"),
    path('admin_package_view',views.admin_package_view,name='admin_package_view'),
    path('package_update/<int:id>/', views.package_update, name='package_update'),
    path('update_package/<int:id>/', views.update_package, name='update_package'),
    path('delete_package/<int:id>',views.delete_package,name='delete_package'),
    

    
]
