from xml.dom.minidom import Document
from django.views import *
from django.urls import  path,include
from django.conf import settings
from django.conf.urls.static import static
from .import views
from django.contrib import admin
from .views import *




urlpatterns =[ path('',views.load_home_page,name='load_home_page'),
               path('load_affiliation_page',views.load_affiliation_page,name='load_affiliation_page'),
               path('admin_login/', admin_login, name='admin_login'),
               path('admin_home/', admin_home, name='admin_home'),
               path('gallery_home/', gallery_home, name='gallery_home'),
               


     ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

