from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import Template, Context
from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from posts.models import *
from module.models import Module
from django.contrib import messages

def view_posts(request):
    listOfPosts = Post.objects.all()
    listOfPostFiles = PostFiles.objects.all()
    context_variable = {
        'posts': listOfPosts,
        'files' : listOfPostFiles
    }
    return render(request, 'posts.html', context_variable)

def view_post(request, id):
    post = Post.objects.get(id=id)
    files = PostFiles.objects.filter(post=post)
    comments = Comment.objects.filter(post=post)
    context_variable = {
        'post': post,
        'files': files,
        'comments': comments
    }
    return render(request, 'post.html', context_variable)

def view_create_post(request):
    if request.user.is_authenticated:
        context_variable = {
            'modules': Module.objects.all()
        }
        return render(request, 'createPost.html', context_variable)
    else:
        return redirect('/posts/')

def create_post(request):
    if request.user.is_authenticated:
        get_author = request.user
        get_postTitle = request.POST['postTitle']
        get_postContent = request.POST['postContent']
        get_moduleID = request.POST['module']
        postObj = Post(
            author=get_author,
            postTitle=get_postTitle,
            postContent=get_postContent
        )
        if request.POST['module']:
            postObj.module = Module.objects.get(pk=get_moduleID)
        postObj.save()
        uploaded_files = request.FILES.getlist('postFile')
        if uploaded_files:
            fs = FileSystemStorage()
            for uploaded_file in uploaded_files:
                get_postImage = fs.save(uploaded_file.name, uploaded_file)
                postImg = PostFiles(
                    post=postObj,
                    file=get_postImage,
                    originalFileName=uploaded_file
                )
                postImg.save()
    return redirect('/posts/')

def view_update_post(request, id):
    get_post_to_update = Post.objects.get(id=id)
    if request.user.is_authenticated and request.user == get_post_to_update.author:
        context_variable = {
            'post': get_post_to_update
        }
        return render(request, 'updatePost.html', context_variable)
    else:
        messages.error(request, "Not authenticated to edit this post")
        return redirect('/posts/')

def update_post(request, id):
    get_post_to_update = Post.objects.get(id=id)
    if request.user.is_authenticated and request.user == get_post_to_update.author:
        get_author = request.user
        get_post_to_update.postTitle = request.POST['postTitle']
        get_post_to_update.postContent = request.POST['postContent']
        get_post_to_update.save()
        uploaded_files = request.FILES.getlist('postFile')
        if uploaded_files:
            fs = FileSystemStorage()
            for uploaded_file in uploaded_files:
                get_postImage = fs.save(uploaded_file.name, uploaded_file)
                postImg = PostFiles(
                    post=get_post_to_update,
                    file=get_postImage,
                    originalFileName=uploaded_file
                )
                postImg.save()
    else:
        messages.error(request, "Not authenticated to edit this post")
    return redirect('/posts/' + str(id))

def delete_post(request, id):
    get_post_to_delete = Post.objects.get(id=id)
    if request.user.is_authenticated and request.user == get_post_to_delete.author:
        get_post_to_delete.delete()
    else:
        messages.error(request, "Not authenticated to edit this post")
    return redirect('/posts/')

def search_post(request):
    if request.user.is_authenticated:
        get_query = request.POST['q']
        match = Post.objects.filter(Q(postTitle__icontains=get_query) | Q(postContent__icontains=get_query))
        context_variable = {
            'posts': match
        }
        return render(request, 'posts.html', context_variable)
    else:
        return redirect('/posts/')

def post_comment(request, id):
    if request.method == 'POST' and request.user.is_authenticated:
        commentObj = Comment(
            commenter= request.user,
            post= Post.objects.get(id=id),
            commentContent= request.POST['commentContent']
        )
        commentObj.save()
    return redirect('/posts/' + str(id))
        
