from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm


def homePage(request):
    posts = Post.objects.all().order_by('-postDate')
    return render(request, "pages/home.html", {
        'posts': posts
    })


def addPost(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("homePage")
    else:
        form = PostForm()

    return render(request, "pages/add-post.html", {
        'form': form
    })


def postDetail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "pages/post-detail.html", {
        'post': post
    })

def deletePost(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect("homePage")

    return render(request, "pages/delete-post.html", {
        'post': post
    })

def editPost(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, request.FILES or None, instance=post)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("postDetail", pk=post.pk)

    return render(request, "pages/edit-post.html", {
        'post': post,
        'form': form
    })