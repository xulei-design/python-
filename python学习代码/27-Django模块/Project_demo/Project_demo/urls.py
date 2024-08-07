"""
URL configuration for Project_demo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from app01 import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/",views.login),
    path('logout/',views.logout),

    # 部门的管理
    path('depart/list/',views.depart_list),
    path('depart/add/',views.depart_add),
    path('depart/delete/',views.depart_delete),
    path('depart/edit/',views.depart_edit),

    # 资产的管理
    path('asset/list/',views.asset_list),
    path('asset/add/',views.asset_add),
    path('asset/edit/',views.asset_edit),
    path('asset/<int:did>/delete/',views.asset_delete),

]
