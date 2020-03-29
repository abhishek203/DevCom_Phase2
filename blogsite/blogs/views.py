from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .forms import UpdateBlogPostForm
from .models import Post
from django.views import generic
from django.shortcuts import get_object_or_404

dic = {}
context = {}
def homepage(request):
    allposts = Post.objects.all()
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            dic['username']=username
            dic['password']=password
            user = authenticate(username=username, password=password)
            
            if user is not None:
               # for posts in allposts:
                #    if posts.users.username==username and posts.users.password==password:
                #login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                context = {'form':form,'username':username,'password':password,'allposts':allposts}
                return render(request,template_name="blogs/dashboard.html",context = context)
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    

    allpost=Post.objects.all()
    context={ 'allpost':allpost }
    context={'allpost':allpost,'form':form}
        
    return render(request,template_name='blogs/homepage.html',context=context)


def edit_blog(request):
    allposts = Post.objects.all()
    for posts in allposts:
        if posts.userdetails.username==dic['username'] and posts.userdetails.password==dic['password']:
            context['post'] = posts
    blog_post = context['post']
    if request.POST:
        form=UpdateBlogPostForm(request.POST or None, request.FILES or None, instance=blog_post)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            context['success_message'] = "Updated"
            blog_post=obj
    form = UpdateBlogPostForm(
        initial={
            "title" : blog_post.title,
            "content" : blog_post.content,
        }
    )
    context['form'] = form
    return render(request, 'blogs/edit_blog.html',context)

