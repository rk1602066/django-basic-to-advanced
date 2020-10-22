blog/views.py:
.................
@login_required
def post_new(request):
    [...]
    
    
try url:http://127.0.0.1:8000/post/new/
Page not found (404)
____________________________________________________________
#Log in users:
------------------
Django is "batteries included", someone has done the hard work for us, so we will make further use of the authentication tools provided
____________________________________________________________________________________________________________________________________________

#mysite/urls.py:
------------------
from django.contrib.auth import views
path('accounts/login/', views.LoginView.as_view(), name='login'),
path('accounts/logout/', views.LogoutView.as_view(), name='logout'),
____________________________________________________________________________________________________________________________________________

blog/templates/registration>login.html:
-------------------------------------------
{% extends "blog/base.html" %}
 
{% block content %}
    {% if form.errors %}
        <p>Your username and password didn't match. Please try again.</p>
    {% endif %}
 
    <form method="post" action="{% url 'login' %}">
    {% csrf_token %}
        <table>
        <tr>
            <td>{{ form.username.label_tag }}</td>
            <td>{{ form.username }}</td>
        </tr>
        <tr>
            <td>{{ form.password.label_tag }}</td>
            <td>{{ form.password }}</td>
        </tr>
        </table>
 
        <input type="submit" value="login" />
        <input type="hidden" name="next" value="{{ next }}" />
    </form>
{% endblock %}
____________________________________________________________________________________________________________________________________________
#add a setting to mysite/settings.py:

LOGIN_REDIRECT_URL = '/'
so that when the login page is accessed directly, it will redirect a successful login to the top-level index (the homepage of our blog)

We already set things up so that only authorized users (i.e. us) see the buttons for adding and editing posts.
Now we want to make sure a login button appears for everybody else.

#blog/templates/blog/base.html
-----------------------------------
<a href="{% url 'login' %}" class="top-menu"><span class="glyphicon glyphicon-lock"></span></a>






