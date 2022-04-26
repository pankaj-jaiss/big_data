"""assignment_2_project URL Configuration

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
import imp
from django.contrib import admin
from django.urls import path,include
from user_login import views 
urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", views.user_login,name='login'),
    path('index/',views.index_page,name='index'),
    # path('migration1/',views.ResourceMigration.as_view(),name='migration1'),
    path('test_connection/',views.TestConnection.as_view(),name='test_connection'),
    # path('test_connection/',views.test_connnection,name='test_connection'),

    path('logout/',views.user_logout,name='logout'),
    path('migration2/',views.migration2_page,name='migration2'),
    path('all_table/',views.get_table_names,name='all_table'),
    path('proceed/',views.proceed, name='proceed'),



     
]
