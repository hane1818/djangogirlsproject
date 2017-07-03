from django.shortcuts import render, HttpResponse
from .models import Post


"""def hello(request):
    return render(request, 'hello.html', {'CLIENT_ID': os.environ.get('CLIENT_ID')})"""

def home(request):
    post_list = Post.objects.all()

    """user_mail_topic = '寄送的標題'
    user_messgae = '內容'
    # 要寄送的對象
    to_list = [
        'hane0131@gmail.com',
    ]
    # Send User Email STMP
    send_mail(
        user_mail_topic,
        user_messgae,
        settings.EMAIL_HOST_USER, to_list,
        fail_silently=False)
    """
    return render(request, 'home.html', {
        'post_list': post_list,
    })

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'post.html', {'post': post})

def call_back(request):
    return HttpResponse(request.GET.get("hub_challenge"))
