"""
URL configuration for hello project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from home import views
from django.conf import settings 
from django.conf.urls.static import static
# from django.urls import path, include
from django.urls import path, include
from django.contrib.auth import views as auth_views

admin.site.site_header = "Shivam pvt ltd Admin"
admin.site.site_title = "Shivam private limited Admin portal"
admin.site.index_title = "Welcome to Shivam Private Ltd"

urlpatterns = [
   path('admin/', admin.site.urls),
   path('', include('home.urls')),  
   
   path("", views.index, name ='home'),
   path("about", views.about, name = 'about'),
   path("services", views.services, name = 'services'),
   path("contact", views.contact, name = 'contact'),
   path("login/", auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('privacy/', views.privacy_policy, name='privacy_policy'),
   

]

