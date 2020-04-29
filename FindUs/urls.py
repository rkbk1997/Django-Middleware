"""FindUs URL Configuration

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
from django.urls import path
from findusapp.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name=''),
    path('index',index,name='index'),
    path('login',Login,name="login"),
    path('logout',Logout,name='logout'),
    path('reg',registationpage,name='reg'),
    path('addcate',addcate,name='addcate'),
    path('userview',userview,name='userview'),
    path('passwordmail',passwordmail,name='passwordmail'),
    path('subcatepage',subcatepage,name='subcatepage'),
    path('service',service,name='service'),
    path('^edit_delete_cate/(?P<sid>[0-9]+)/(?P<option>[\w-]+)/$',Edit_Delete_cate,name="edit_delete_cate"),
    path('^edit_delete_subcate/(?P<sid>[0-9]+)/(?P<option>[\w-]+)/$',Edit_Delete_subcate,name="edit_delete_subcate"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

