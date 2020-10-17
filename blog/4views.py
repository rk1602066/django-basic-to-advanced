from django.http import HttpResponse,render

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
    
def post_list(request):
  return render(request,'blog/post_list.html',{})
  
/*here render({}):{}-> is a python dictionary 
# we can use like bellow:
#dict_name{
"a":1,"b":2
}
return render(request,'blog/post_list.html',dict_name)

it will try to find post_list.html file from blog/templates/blog folder
so we have to create templates/blog/post_list.html within blog folder
*/
