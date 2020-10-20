#create new post and edit post

blog
   └── forms.py

blog/forms.py:
from django import forms
from .models import Post
 
class PostForm(forms.ModelForm): 
    class Meta:
        model = Post
        fields = ('title', 'text',)


#blog/templates/blog/base.html. We will add a link in div named page-header:
 <a href="{% url 'post_new' %}" class="top-menu"><span class="glyphicon glyphicon-plus"></span></a>
 this will display a plus sign for us.
 
 #blog/urls.py and add a line:
path('post/new', views.post_new, name='post_new'),

#Edit form
Now we know how to add a new form. But what if we want to edit an existing one? This is very similar to what we just did. Let's create some important things quickly.
Open blog/templates/blog/post_detail.html and add the line

<a class="btn btn-default" href="{% url 'post_edit' pk=post.pk %}"><span class="glyphicon glyphicon-pencil"></span></a>


In blog/urls.py we add this line:
path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),


#create new post
#Let's open blog/views.py and add this at the very end of the file:
blog/views.py:
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
    

#edit post:
#blog/templates/blog/post_edit.html
{% extends 'blog/base.html' %}
 
{% block content %}
    <h1>New post</h1>
    <form method="POST" class="post-form">{% csrf_token %}
        {{ form.as_p }}
        <button type="submit" class="save btn btn-default">Save</button>
    </form>
{% endblock %}


edit:
blog/templates/blog/post_detail.html
<a class="btn btn-default" href="{% url 'post_edit' pk=post.pk %}"><span class="glyphicon glyphicon-pencil"></span></a>
this will add a pencil for edit post

blog/urls.py we add this line:
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    
    
blog/views.py

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
        
        
{% if user.is_authenticated %}
    <a href="{% url 'post_new' %}" class="top-menu"><span class="glyphicon glyphicon-plus"></span></a>
{% endif %}

{% if user.is_authenticated %}
     <a class="btn btn-default" href="{% url 'post_edit' pk=post.pk %}"><span class="glyphicon glyphicon-pencil"></span></a>
{% endif %}
    return render(request, 'blog/post_edit.html', {'form': form})    
