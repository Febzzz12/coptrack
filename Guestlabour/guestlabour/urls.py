"""guestlabour URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from guestlabourapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index),
    path('',views.index),

    path('adminhome/',views.adminhome),
    path('labourhome/',views.labourhome),
    path('policehome/',views.policehome),
    path('userhome/',views.userhome),
    path('login/',views.login),
    path('userregister/',views.userregister),
    path('labourregister/',views.labourregister),
    path('policeregister/',views.policeregister),

    path('adminviewcomplaint/',views.adminviewcomplaint),
    path('adminviewlabour/',views.adminviewlabour),
    path('adminviewpolice/',views.adminviewpolice),
    path('adminviewuser/',views.adminviewuser),
    path('adminviewbooking/',views.adminviewbooking),
    path('adminupdatestatus/',views.adminupdatestatus),

    path('policeapprovelabour/',views.policeapprovelabour),
    path('policeapproved/',views.policeapproved),
    path('policereject/',views.policereject),
    path('policereplycomplaints/',views.policereplycomplaints),
    path('policeviewcomplaints/',views.policeviewcomplaints),

    path('useraddcomplaint/',views.useraddcomplaint),
    path('userviewlabour/',views.userviewlabour),
    path('userbooklabour/',views.userbooklabour),
    path('userviewbooking/',views.userviewbooking),
    path('payment1/',views.payment1),
    path('payment2/',views.payment2),
    path('payment3/',views.payment3),
    path('payment4/',views.payment4),
    path('payment5/',views.payment5),

    path('labourviewapprovedbooking/',views.labourviewapprovedbooking),
    path('labourviewcertificate/',views.labourviewcertificate),


]
