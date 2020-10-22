#blog/views.py:
.....................

from django.shortcuts import render,get_object_or_404,redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm

# Create your views here.

def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now())
	return render(request,'blog/post_list.html',{'posts':posts})


def post_detail(request,pk):
	post = get_object_or_404(Post,pk=pk)
	return render(request,'blog/post_detail.html',{'post':post})	


def post_new(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			#post.published_date = timezone.now()
			post.save()
			return redirect('post_detail',pk=post.pk)
	else:		
		form = PostForm()
	return render(request,'blog/post_edit.html',{'form':form})


def post_edit(request, pk):
	post = get_object_or_404(Post, pk=pk)
	if request.method == "POST":
	    form = PostForm(request.POST, instance=post)
	    if form.is_valid():
	        post = form.save(commit=False)
	        post.author = request.user
	        #post.published_date = timezone.now()
	        post.save()
	        return redirect('post_detail', pk=post.pk)
	else:
	    form = PostForm(instance=post)
	return render(request, 'blog/post_edit.html', {'form': form})


def post_draft_list(request):
	posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
	return render(request,'blog/post_draft_list.html',{'posts':posts})	


def post_publish(request,pk):
	post = get_object_or_404(Post,pk=pk)
	post.publish()
	return redirect('post_detail',pk=pk)

	
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')
    
...............................................................................................

blog/urls.py:
...........................
from django.urls import path
from . import views

urlpatterns=[
		path('',views.post_list,name = 'post_list'),
		path('post/<int:pk>/',views.post_detail,name='post_detail'),
		path('post/new', views.post_new, name='post_new'),
		path('post/<int:pk>/edit/',views.post_edit,name='post_edit'),
		path('drafts/',views.post_draft_list,name='post_draft_list'),
		path('post/<int:pk>/publish/',views.post_publish,name='post_publish'),
		path('post/<int:pk>/remove/', views.post_remove, name='post_remove'),
]
......................................................................................................


blog/base.html:
..........................
<div class="page-header">
            {% if user.is_authenticated %}
            <a href="{% url 'post_new' %}" class="top-menu"><span class="glyphicon glyphicon-plus"></span></a>
            <a href="{% url 'post_draft_list' %}" class="top-menu"><span class="glyphicon glyphicon-edit"></span></a>
            {% endif %}
            <h1><a href="/">My Blog</a></h1>
 </div>
 .................................................................................
 
 
 #blog/forms.py:
 ...............
from django import forms
from .models import Post

class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = {'title','text'}
........................................................................................

#blog/post_list.html
........................
 {% extends 'blog/base.html' %}

{% block content %}
           
 {% for post in posts %}
        <div class="post">
            <div class="date">
                {{ post.published_date }}
            </div>
            <h1><a href="{% url 'post_detail' pk=post.pk %}">{{ post.title }}</a></h1>
            <p>{{ post.text|linebreaksbr }}</p>
        </div>
    {% endfor %}

     {% endblock %}
........................................................................................

#blog/post_detail.html:
.......................
{% extends 'blog/base.html'%}

{% block content %}

<div class="post">
        {% if post.published_date %}
    		<div class="date">
       		 {{ post.published_date }}
    		</div>
		{% else %}
    		<a class="btn btn-default" href="{% url 'post_publish' pk=post.pk %}">Publish</a>
		{% endif %}

        {% if user.is_authenticated %}
        <a class="btn btn-default" href="{% url 'post_edit' pk=post.pk %}"><span class="glyphicon glyphicon-pencil"></span></a>

        <a class="btn btn-default" href="{% url 'post_remove' pk=post.pk %}"><span class="glyphicon glyphicon-remove"></span></a>
        
        {% endif %}
        <h4><strong>Author:</strong> {{post.author}}</h4>
        <h1>{{ post.title }}</h1>
        <p>{{ post.text|linebreaksbr }}</p>
    </div>

{% endblock %}
...............................................................................................................

#blog/post_edit.html:
.........................
{% extends 'blog/base.html' %}

{% block content %}
<h1>New post</h1>
<form method="POST">{% csrf_token %}
{{ form.as_p}} 
<button type="submit" class="save btn=default">save</button>
</form>
{% endblock %}
................................................................................................................

#blog/post_draft.html:
.........................
{% extends 'blog/base.html' %}

{% block content %}
	{% for post in posts %}
        <div class="post">
            <p class="date">created: {{ post.created_date|date:'d-m-Y' }}</p>
            <h1><a href="{% url 'post_detail' pk=post.pk %}">{{ post.title }}</a></h1>
            <p>{{ post.text|truncatechars:200 }}</p>
        </div>
    {% endfor %}

{% endblock %}
........................................................................................................................

#link to css.:
...............
 <link rel="stylesheet" href="{% static 'css/blog.css' %}">
 blog/static/css>blog.css
 blog/templates/blog>base.html
    

