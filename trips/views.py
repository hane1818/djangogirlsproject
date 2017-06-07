from django.shortcuts import render
from .models import Post


def hello(request):
    return render(request, 'hello.html', {'CLIENT_ID': os.environ.get('CLIENT_ID')})

def home(request):
    post_list = Post.objects.all()
    return render(request, 'home.html', {
        'post_list': post_list,
    })

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post.html', {'post': post})
