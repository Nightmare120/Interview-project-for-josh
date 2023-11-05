"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, re_path
from dashboard.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    
    re_path("page",show_html_page),
    re_path("dashboard/create-project",create_project_page),
    re_path("save",save_project),
    re_path("create",create_new_project),
    re_path("delete",delete_project),
    re_path("dashboard/project",project),
    # re_path("dashboard/project",project),
    re_path("dashboard",dashboard),
]
