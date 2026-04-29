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
from django.urls import path,include
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("admin_app.urls")),
    path('',include("user_app.urls")),
    path('',include("package_app.urls")),
    path('',views.index,name='index'),
    path('home',views.home),
    path('about',views.about),
    path('trips',views.trips),
    path('blog',views.blog),
    path('contact',views.contact),
    path('register',views.register),
    path('login',views.login,name='login'),
    path('costarica',views.costarica),
    path('logout',views.logout),
    # path('booking',views.book),
    path('tempbooking', views.tempbooking, name='tempbooking'),
    path('book_update/<int:id>',views.book_update,name="book_update"),
    path('payment_success/', views.payment_success, 
    name='payment_success'),
    path('my_bookings/', views.my_bookings, name='my_bookings'),

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
