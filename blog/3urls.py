mysite/urls.py  #this is the main urls.py of the project

from django.urls import path, include
from django.contrib import admin
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
]

#here we include blog.urls so that django could reached to requested urls within blog/urls.py



blog/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]

# for every request surver will renponse with a view that is insite blog/views.py
#here post_list is a method in blog/views.py whith return html files render templates 
