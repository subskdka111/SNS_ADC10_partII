from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import Template, Context
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from posts.models import Post

# Create your views here.
def view_posts(request):
    listOfPosts = Post.objects.all()
    context_variable = {
        'posts': listOfPosts
    }
    return render(request, 'posts.html', context_variable)

def view_post(request, id):
    post = Post.objects.get(id=id)
    context_variable = {
        'post': post
    }
    return render(request, 'post.html', context_variable)

def view_create_post(request):
    if request.user.is_authenticated:
        return render(request, 'createPost.html')
    else:
        return redirect('/posts/')

def create_post(request):
    if request.user.is_authenticated:
        get_author = request.user
        get_postTitle = request.POST['postTitle']
        get_postContent = request.POST['postContent']
        uploaded_file = request.FILES.get("postFile")

        if uploaded_file:
            fs = FileSystemStorage()
            get_postImage = fs.save(uploaded_file.name, uploaded_file)
            postObj = Post(author=get_author, postTitle=get_postTitle, postContent=get_postContent, postFiles=get_postImage)
        else:
            postObj = Post(author=get_author, postTitle=get_postTitle, postContent=get_postContent)

        postObj.save()
    return redirect('/posts/')

def view_update_post(request, id):
    get_post_to_update = Post.objects.get(id=id)
    if request.user.is_authenticated and request.user == get_post_to_update.author:
        context_variable = {
            'post': get_post_to_update
        }
        return render(request, 'updatePost.html', context_variable)
    else:
        return HttpResponse("Error:")

def update_post(request, id):
    get_post_to_update = Post.objects.get(id=id)
    if request.user.is_authenticated and request.user == get_post_to_update.author:
        get_author = request.user
        get_post_to_update.postTitle = request.POST['postTitle']
        get_post_to_update.postContent = request.POST['postContent']
        get_post_to_update.save()
        return redirect('/posts/')
    else:
        return HttpResponse("Error:")

def delete_post(request, id):
    get_post_to_delete = Post.objects.get(id=id)
    if request.user.is_authenticated and request.user == get_post_to_delete.author:
        get_post_to_delete.delete()
    return redirect('/posts/')

def search_post(request):
    if request.user.is_authenticated:
        get_query = request.POST['q']
        match = Post.objects.filter(
            Q(postTitle__icontains=get_query) | Q(postContent__icontains=get_query))
        context_variable = {
            'posts': match
        }
        return render(request, 'posts.html', context_variable)
    else:
        return redirect('/posts/')
