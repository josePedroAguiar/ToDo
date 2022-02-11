"""toDo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from toDoApp import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),

    #
    path('signup/', views.signup, name="signup"),
    path('logout/', views.logout ,name="logout"),
    path('login/', views.login ,name="login"),

    #
    path('', views.home, name="home"),
    path('create/', views.createToDo ,name="createToDo"),
    path('current/', views.currentToDo ,name="currentToDo"),
    path('completed/', views.completedToDo,name="completedToDo"),
    path('todo/<int:todo_pk>', views.viewToDo, name="viewToDo"),
    path('todo/<int:todo_pk>/complete/', views.completeToDo, name="completeToDo"),
    path('todo/<int:todo_pk>/delete/', views.deleteToDo, name="deleteToDo"),
    path('todo/<int:todo_pk>/reverse/', views.reverseToDo, name="reverseToDo"),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)