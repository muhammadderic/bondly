from django.shortcuts import redirect, render
from .models import Post

def home(request):
  return render(request, 'home.html')

def add_post(request):
  if (request.method == 'POST'):
    title = request.POST.get('title')
    content = request.POST.get('content')

    post = Post(title=title, content=content)
    post.save()
    return redirect('home')

  return render(request, 'add_post.html')