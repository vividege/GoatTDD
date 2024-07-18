"""
URL configuration for superlists project.

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

    urls.py文件定义如何把URL映射到视图函数上
"""
from django.urls import re_path
from lists.views import home_page, view_list, new_list, add_item

urlpatterns = [
    re_path(r'^$', home_page, name='home'),
    re_path(r'^(\d+)/$', view_list, name='view_list'),
    re_path(r'^(\d+)/add_item$', add_item, name='add_item'),
    re_path(r'^new$', new_list, name='new_list'),
]
