"""ku URL Configuration

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
from django.contrib.auth import views as auth_views

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from ku_app.views import (
    base_view,
    create_docx_document1,
    create_docx_document2, 
    )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('client/', include('ku_app.urls')),
    path('login/', auth_views.LoginView.as_view(), name = 'login'),
    path('', base_view, name = 'base'),
    path('make_doc1/', create_docx_document1, name = 'make_doc1'),
    path('make_doc2/', create_docx_document2, name = 'make_doc2'),
    path('save_data/', TemplateView.as_view(template_name = 'save_data.html'), name = 'save_data'),
]