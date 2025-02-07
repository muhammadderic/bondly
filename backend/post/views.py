from django.shortcuts import redirect, render
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