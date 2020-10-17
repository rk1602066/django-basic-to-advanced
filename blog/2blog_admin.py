from django.contrib import admin
from .models import Post
 
admin.site.register(Post)
//admin panal theke database er post add, edit,delete korte ekhane Post(models-> er classname) k register korte hobe


#create super user
venv: python manage.py createsuperuser
