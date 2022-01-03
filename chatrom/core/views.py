from django.shortcuts import render
from .models import Post

# Create your views here.
def index(response):
    p = Post.objects.all()
    return render(response, 'index.html', {'p': p})