"""permission URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include,re_path
from rbac.views import role
from rbac.views import user
from rbac.views import menu

app_name = '[rbac]'
urlpatterns = [

    #角色表
    re_path(r'^role/list/$',role.role_list, name='role_list'),
    re_path(r'^role/add/$',role.role_add,name='role_add'),
    re_path(r'^role/edit/(?P<pk>\d+)/$',role.role_edit,name='role_edit'),
    re_path(r'^role/del/(?P<pk>\d+)/$',role.role_del,name='role_del'),

    #用户表
    re_path(r'^user/list/$',user.user_list, name='user_list'),
    re_path(r'^user/add/$',user.user_add,name='user_add'),
    re_path(r'^user/edit/(?P<pk>\d+)/$',user.user_edit,name='user_edit'),
    re_path(r'^user/del/(?P<pk>\d+)/$',user.user_del,name='user_del'),
    re_path(r'^user/reset_pwd/(?P<pk>\d+)/$',user.user_reset_pwd,name='user_reset_pwd'),


    #权限表（一级菜单）
    re_path(r'^menu/list/$',menu.menu_list, name='menu_list'),
    re_path(r'^menu/add/$',menu.menu_add, name='menu_add'),
    re_path(r'^menu/edit/(?P<pk>\d+)/$',menu.menu_edit, name='menu_edit'),
    re_path(r'^menu/del/(?P<pk>\d+)/$',menu.menu_del, name='menu_del'),

    #权限表（二级菜单）
    re_path(r'^second_menu/add/(?P<menu_id>\d+)/$',menu.second_menu_add, name='second_menu_add'),
    re_path(r'^second_menu/edit/(?P<pk>\d+)/$',menu.second_menu_edit, name='second_menu_edit'),
    re_path(r'^second_menu/del/(?P<pk>\d+)/$',menu.second_menu_del, name='second_menu_del'),

    #权限管理
    re_path(r'^permission/add/(?P<second_menu_id>\d+)/$',menu.permission_add, name='permission_add'),
    re_path(r'^permission/edit/(?P<pk>\d+)/$',menu.permission_edit, name='permission_edit'),
    re_path(r'^permission/del/(?P<pk>\d+)/$',menu.permission_del, name='permission_del'),


    #发现项目中的url
    re_path(r'^permission/multi_permissions/$',menu.multi_permissions, name='multi_permissions'),
    re_path(r'^permission/multi_permissions_del/(?P<pk>\d+)/$',menu.multi_permissions_del, name='multi_permissions_del'),


    #权限分配
    re_path(r'^permission/distribute/$',menu.permission_distribute, name='permission_distribute'),
]
