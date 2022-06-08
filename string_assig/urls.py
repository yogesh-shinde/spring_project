"""string_assig URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from venv import create
from django.contrib import admin
from django.urls import path
from myapp.views import CourseAPIView
from myapp.views import StudentAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('course/', CourseAPIView.as_view()),
    path('course/<int:pk>/', CourseAPIView.as_view()),
    path('student/', StudentAPIView.as_view()),
]
