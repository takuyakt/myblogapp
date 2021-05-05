from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def index(request):
    # return HttpResponse("Hello world! このページは投稿のインデックスです。")
    posts = Post.objects.order_by('-published')
    return render(request, 'posts/index.html', {'posts' : posts})

# Create your views here.
