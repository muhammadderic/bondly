from django.shortcuts import redirect, render, get_object_or_404
from .models import Post

def home(request):
  post_list = Post.objects.all()
  return render(request, 'home.html', {'post_list': post_list})

def add_post(request):
  if (request.method == 'POST'):
    title = request.POST.get('title')
    content = request.POST.get('content')

    post = Post(title=title, content=content)
    post.save()
    return redirect('home')

  return render(request, 'add_post.html')

def update_post(request, post_id):
  post = get_object_or_404(Post, post_id=post_id)

  if (request.method == 'POST'):
    title = request.POST.get('title')
    content = request.POST.get('content')

    post.title = title
    post.content = content
    post.save()
    return redirect('home')

  return render(request, 'update_post.html', {'post': post})

def delete_post(request, post_id):
  post = get_object_or_404(Post, post_id=post_id)
  post.delete()
  return redirect('home')