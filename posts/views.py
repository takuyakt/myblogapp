from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world! このページは投稿のインデックスです。")

# Create your views here.
