"""list_task URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from webapp.views import task_view, \
    list_of_task_view, \
    task_create_view, \
    remove_view, \
    task_update_view

HOMEPAGE_URL = 'task/'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task/<int:id>', task_view,  name='task-view'),
    path('', list_of_task_view, name='list-view'),
    path('add/', task_create_view, name='task-add'),
    path('remove/<int:id>', remove_view, name='delete-task'),
    path('update/<int:id>', task_update_view, name='task-update')

    ,

]

