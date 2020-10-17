(myvenv) ~/myblog$ python manage.py shell


Post.objects.all()
Traceback (most recent call last):
      File "<console>", line 1, in <module>
NameError: name 'Post' is not defined

from blog.models import Post
Post.objects.all()
<QuerySet [<Post: my post title>, <Post: another post title>]>


from django.contrib.auth.models import User
User.objects.all()
Out[6]: <QuerySet [<User: rakib1602066>]>

#create users instance variable
me=User.objects.get(username='rakib1602066')
me
Out[11]: <User: rakib1602066>


#create new object
 Post.objects.create(author=me, title='Sample title', text='Test')
<Post: Sample title>

#query:
In [14]: Post.objects.all()
Out[14]: <QuerySet [<Post: First post>, <Post: Second post>, <Post: Third post>, <Post: Sample title>]>

In [15]: Post.objects.filter(author=me)
Out[15]: <QuerySet [<Post: First post>, <Post: Second post>, <Post: Third post>, <Post: Sample title>]>

In [16]: Post.objects.filter(title__contains='title')
Out[16]: <QuerySet [<Post: Sample title>]>


from django.utils import timezone
Post.objects.filter(published_date__lte=timezone.now())
<QuerySet []>


Unfortunately, the post we added from the Python console is not published yet. But we can change that! First get an instance of a post we want to publish:

>>> post = Post.objects.get(title="Sample title")
And then publish it with our publish method:

>>> post.publish()
Now try to get list of published posts again (press the up arrow key three times and hit enter):

>>> Post.objects.filter(published_date__lte=timezone.now())
<QuerySet [<Post: Sample title>]>



QuerySets also allow you to order the list of objects. Let's try to order them by created_date field:

>>> Post.objects.order_by('created_date')
<QuerySet [<Post: Sample title>, <Post: Post number 2>, <Post: My 3rd post!>, <Post: 4th title of post>]>
We can also reverse the ordering by adding - at the beginning:

>>> Post.objects.order_by('-created_date')
<QuerySet [<Post: 4th title of post>,  <Post: My 3rd post!>, <Post: Post number 2>, <Post: Sample title>]>


You can also combine QuerySets by chaining them together:

>>> Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
<QuerySet [<Post: Post number 2>, <Post: My 3rd post!>, <Post: 4th title of post>, <Post: Sample title>]>
This is really powerful and lets you write quite complex queries.

Cool! You're now ready for the next part! To close the shell, type this:

>>> exit()
$
