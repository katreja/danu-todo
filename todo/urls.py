"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from todoapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('registration/signup/', views.SignUpView.as_view(), name='signup'),
    path('profiles/profile/', views.ProfileView.as_view(), name ='profile'),
    path('profiles/<int:id>/edit', views.ProfileUpdateView.as_view(), name ='profile-update'),
    path('admin/', admin.site.urls),
    path('', views.HomeView.as_view(), name='home'),
    path('todoes/', views.TodoAllView.as_view(), name='todo-all'),
    path('todoes/<int:pk>', views.DetailTodoView.as_view(), name='todo-detail' ),
    path('todoes/<int:id>/edit', views.TodoEditView.as_view(), name='todo-edit'),
    path('todoes/create/', views.TodoCreateView.as_view(), name='todo-create'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
