from django.shortcuts import render, redirect
from post.models import Post

def index_view(request):
    return render(request, 'index.html')

def post_create_view(request):
    if request.method == 'GET':
        return render(request, 'post_create.html')
    elif request.method == "POST":
        post = Post.objects.create(
             author=request.POST.get('author'),
             body=request.POST.get('body')
        )
        return render(request, 'post_detail.html',context= {'post':post})






