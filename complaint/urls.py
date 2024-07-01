"""complaint URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from policeapp import views as policeapp_views
from mainapp import views as mainapp_views
from userapp import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',mainapp_views.index,name='index'),
    path('about',mainapp_views.about,name='about'),
    path('contact',mainapp_views.contact,name='contact'),
    
    
   #police or admin 
   path('police_login',policeapp_views.police_login,name='police_login'),
   path('police_dashboard',policeapp_views.police_dashboard,name='police_dashboard'),
   path('view_complient',policeapp_views.view_complient,name='view_complient'),
   path('update_complient',policeapp_views.update_complient,name='update_complient'),
   path('Complete/<int:id>/',policeapp_views.Complete,name='Complete'),
   path('register/<int:id>/',policeapp_views.register,name='register'),
   path('discard/<int:id>/',policeapp_views.discard,name='discard'),
   path('fill_FIR/<int:id>/',policeapp_views.fill_FIR,name='fill_FIR'),
   path('fill_NCR<int:id>/',policeapp_views.fill_NCR,name='fill_NCR'),
   path('view_feedback',policeapp_views.view_feedback,name="view_feedback"),
   path('all_complaints',policeapp_views.all_complaints,name="all_complaints"),
   
   #user
   
   path('user_register',user_views.user_register,name='user_register'),
   path('user_login',user_views.user_login,name='user_login'), 
   path('user_index',user_views.user_index,name='user_index'),
   path('user_profile',user_views.user_profile,name='user_profile'),
   path('add_complaint',user_views.add_complaint,name='add_complaint'),  
   path('check_complaint',user_views.check_complaint,name='check_complaint'),  
   path('user_feedback',user_views.user_feedback,name='user_feedback'),   
   path('all_complaints',user_views.all_complaints,name='all_complaints'),
#    path('verify',user_views.verify,name='verify'),
      
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
