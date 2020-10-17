from django.shortcuts import render
from django.utils import timezone
from .models import Post
 
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
    

.html:

blog/templates/blog/post_list.html

{{ posts }}

{% for post in posts %}
    {{ post }}
{% endfor %}


finally:

blog/templates/blog/post_list.html::

<div>
    <h1><a href="/">My Blog</a></h1>
</div>
 
{% for post in posts %}
    <div>
        <p>published: {{ post.published_date }}</p>
        <h1><a href="">{{ post.title }}</a></h1>
        <p>{{ post.text|linebreaksbr }}</p>
    </div>
{% endfor %}


static files:
 
blog
├── blog
│   ├── migrations  
│   ├── static
│   └── templates
└── mysite

myblog
└─── blog
     └─── static
          |└─── css
          |     └─── blog.css
          |----js
                |__blog.js
     
so django will looking for the static files in these directory     


