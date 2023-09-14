"""
URL configuration for Concreteview project.

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
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('studentlist/',views.studentList.as_view())
    # path('studentcreate/',views.studentCreate.as_view())
    # path('studentretrieve/<int:pk>',views.studentRetrieve.as_view())
    # path('studentdestroy/<int:pk>',views.studentDestroy.as_view())
    
    # path('studentlistcreate/',views.studentListCreate.as_view()),
    # path('studentretrieveupdate/<int:pk>',views.studentRetrieveUpdate.as_view())
    # path('studentretrievedestroy/<int:pk>',views.studentRetrieveDestroy.as_view())
]
