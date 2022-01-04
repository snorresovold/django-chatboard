from django.shortcuts import render
from .models import Post
from .forms import CreateNewPost

# Create your views here.
def home(request):
    return render(request, "core/home.html", {"posts":Post.objects.all()})

def create(request):
    if request.method == "POST":
        form = CreateNewPost(request.POST)

        if form.is_valid():
            u = request.user
            n = form.cleaned_data["name"]
            c = form.cleaned_data["content"]
            tt = Post(user = u, name = n, content = c)
            tt.save()
    else:
        form = CreateNewPost()
    return render(request, "core/create.html", {"form": form})